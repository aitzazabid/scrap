from django.test.utils import override_settings
from django.conf import settings
import os


@override_settings(DEBUG=True)
def test_debug(self):
    assert settings.DEBUG
DEBUG = True
BASE_DIR = os.path.dirname(__file__)
# local_database_settings

DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': 1000,
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wedget',
        'USER': 'postgres',
        'PASSWORD': 'emblemtech',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}


MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'client',
    'webadmin'
)
