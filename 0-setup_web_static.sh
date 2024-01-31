#!/usr/bin/env bash
#script to set up servers for web static deployment

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "<html><head></head><body>Hello World!</body></html>" | sudo tee /data/web_static/releases/test/index.htmlsudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
nginx_config="/etc/nginx/sites-available/default"
sudo sed -i "/server_name _;/a \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}" $nginx_config
