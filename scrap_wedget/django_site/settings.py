"""
Django settings file.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/

Double-check these settings against recommended deployment settings here:
https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
"""
import os
from django.contrib.messages import constants as messages

BASE_DIR = os.path.dirname(__file__)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '28572ijfjdnngmkkw74633134htsljdfnlvspqhr4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Ideally this should NOT be a wildcard.
ALLOWED_HOSTS = ['*']


DATE_FORMAT = 'Y/m/d H:i:s'

DEBUG_WORK_QUEUE = False

# Configure CORS
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1:8000',
)


# If True, SMS messages are merely logged, not sent.
DISABLE_SMS = False

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/static/'

STATIC_URL = '/static/'

MEDIA_ROOT = '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

LOGIN_URL = '/webadmin/login'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MESSAGE_TAGS = {
    messages.SUCCESS: 'notification-success',
    messages.ERROR: 'notification-fail',
}

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'client',
    'webadmin',


)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = False


# Import local settings
try:
    from local_settings import *
except:
    print('Local settings not imported.')

