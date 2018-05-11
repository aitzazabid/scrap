
echo "Stoping and removing upstart jobs"
sudo stop scrap-uwsgi
sudo rm /etc/init/scrap-uwsgi.conf

echo "Removing nginx file"
sudo /etc/init.d/nginx stop
sudo rm /etc/nginx/sites-enabled/scrap.conf
sudo rm /etc/nginx/sites-available/scrap.conf

echo "Restarting nginx"
sudo /etc/init.d/nginx start
