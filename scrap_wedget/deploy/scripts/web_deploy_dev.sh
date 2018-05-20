#!/bin/bash
cd /scrap/scrap_wedget/deploy

echo "Copying systemd unit"
sudo cp systemd/scrap-uwsgi.service /lib/systemd/system
sudo systemctl daemon-reload

echo "Restarting uwsgi"
sudo systemctl stop scrap-uwsgi
sudo systemctl enable scrap-uwsgi
sudo systemctl start scrap-uwsgi

echo "Copying DEV nginx config"
sudo cp nginx/scrap_wedget.conf /etc/nginx/sites-available/scrap_wedget.conf
sudo ln -s -f /etc/nginx/sites-available/scrap_wedget.conf /etc/nginx/sites-enabled/scrap_wedget.conf

echo "Restarting nginx"
sudo systemctl restart nginx
