#!/bin/bash

echo "Stoping and removing systemctl unit"
sudo systemctl stop scrap-uwsgi
sudo rm /lib/systemd/system/scrap-uwsgi.service

echo "Removing nginx file"
sudo systemctl stop nginx
sudo rm /etc/nginx/sites-enabled/scrap_wedget.conf
sudo rm /etc/nginx/sites-available/scrap_wedget.conf

echo "Restarting nginx"
sudo systemctl start nginx
