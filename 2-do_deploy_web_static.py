#!/usr/bin/python3
from os.path import exists
from fabric.api import *
"""Fabfile to:
    Distribute a specific backup of the web static files on all our web servers
    and configurates the server to serve the new files.
"""


env.hosts = ['35.231.32.184', '35.185.113.169']
env.user = 'ubuntu'


def do_pack():
    """Function to create the backup of the project

    Returns: Path to the backup or None otherwise.
    """
    local('mkdir -p ./versions', capture=False)
    date = datetime.now()
    date_args = (date.year, date.month, date.day,
                 date.hour, date.minute, date.second)
    name_backup = './versions/web_static_{}{}{}{}{}{}.tgz'.format(*date_args)
    local('tar -cvzf ' + name_backup + ' web_static/')

    return name_backup if exists(name_backup) else None


def do_deploy(archive_path):
    """Fabric script to upload new static files to all servers
    and configure the server to deploy they.

    Arguments:
        archive_path {str} -- The path to the compressed backup
                              that will be deployed.

    Returns:
        bool -- True if all operations have been done correctly,
                otherwise False.
    """
    if not exists(archive_path):
        return False

    deploy_folder = local(
        'basename {} .tgz'.format(archive_path), capture=True)
    deploy_path = '/data/web_static/releases/{}'.format(deploy_folder)
    run('mkdir -p {}'.format(deploy_path))
    put(archive_path, '/tmp')
    with cd('/tmp'):
        run('tar -xzf ./{}.tgz -C {}'.format(deploy_folder, deploy_path))
        run('rm -f ./{}.tgz'.format(deploy_folder))
    with cd(deploy_path):
        run('mv ./web_static/* .')
        run('rm -rf ./web_static')
    serving_path = '/data/web_static/current'
    run('rm -rf {}'.format(serving_path))
    run('ln -s {} {}'.format(deploy_path, serving_path))
    print('New version deployed!')
    return True
