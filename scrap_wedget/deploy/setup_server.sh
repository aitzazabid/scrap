
sudo apt-get install nginx python-setuptools python-dev postgresql libpq-dev libmysqlclient-dev
sudo easy_install pip
sudo pip install uwsgi django psycopg2 boto twilio pycrypto pillow
sudo rm /etc/nginx/sites-enabled/default

echo "Next steps:"
echo "  Add SCRAP_REPO_HOME=<full path to repository> to /etc/environment"
echo "  Create static directory with suitable read access"
echo "  Create database"

echo "Logging"
echo "  uwsgi (python application) log: /var/log/upstart/scrap-uwsgi.log"
echo "  nginx log: /var/log/nginx/error.log"
