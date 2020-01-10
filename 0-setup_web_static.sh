#!/usr/bin/env bash
# Script that configure a Nginx server with:
#   Folders structure for deployment of web_static.
#   Dummy html file to test the server.
#   Deploy the web static folder.

# Variables

path_dummy_test_page='/data/web_static/releases/test/index.html'

new_location='\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n'

sites_conf_file='/etc/nginx/sites-available/default'

# Procedure

# Install Nginx
sudo apt-get update -y
sudo apt-get install nginx -y

# Create Folders structure
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create dummy test page
echo -e '<html>
\t<head>
\t</head>
\t<body>
\tHolberton School
\t</body>
</html>\n' | sudo tee $path_dummy_test_page

# Create symbolic link from test to current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of data to user/group ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx conf to make the site available
sudo sed -i "/server_name _;/ i $new_location" $sites_conf_file

# Restart Nginx service
sudo service nginx restart
