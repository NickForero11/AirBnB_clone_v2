#!/usr/bin/python3
"""Fabfile to:
    Generate a backup of the actual content of the project.
    Save the backup in a certain folder.
    Format the name of the backup with the creation date & time.
"""
from fabric.api import local
from datetime import datetime
from os.path import exists


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
