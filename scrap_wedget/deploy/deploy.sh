cd $SCRAP_REPO_HOME/deploy
hg pull -u

echo "Copying upstart jobs"
sudo cp upstart/scrap-uwsgi.conf /etc/init

echo "Restarting uwsgi"
sudo stop scrap-uwsgi

echo "Restarting work queue"
sudo stop scrap-work

echo "Copying nginx config"
sudo cp nginx/scrap.conf /etc/nginx/sites-available
sudo cp nginx/nginx.conf /etc/nginx/
sudo ln -s -f /etc/nginx/sites-available/scrap.conf /etc/nginx/sites-enabled/scrap.conf
sudo rm /etc/nginx/sites-enabled/default

echo "Restarting nginx"
sudo /etc/init.d/nginx restart

cd $SCRAP_REPO_HOME/django_site
python manage.py collectstatic --noinput

echo "Any migrations should be run manually"
