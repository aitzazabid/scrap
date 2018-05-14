sudo apt install build-essential python-dev nginx postgresql postgresql-client python3-pip
sudo pip3 install django psycopg2 uwsgi requests pytz pycrypto zeep boto3 pillow xmltodict django-crontab pyfcm phonenumbers==8.8.7




sudo rm /etc/nginx/sites-enabled/default

echo "Next steps:"
echo "  Add SCRAP_REPO=<full path to repository> to /etc/environment"
echo "  Create static directory with suitable read access"
echo "  Create database"
