"""
Django settings for myproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
	ON_OPENSHIFT = True
if os.environ.has_key('OPENSHIFT_APP_NAME'):
	DB_NAME = os.environ['OPENSHIFT_APP_NAME']
if os.environ.has_key('OPENSHIFT_POSTGRESQL_DB_USERNAME'):
	DB_USER = os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME']
if os.environ.has_key('OPENSHIFT_POSTGRESQL_DB_PASSWORD'):
	DB_PASSWD = os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD']
if os.environ.has_key('OPENSHIFT_POSTGRESQL_DB_HOST'):
	DB_HOST = os.environ['OPENSHIFT_POSTGRESQL_DB_HOST']
if os.environ.has_key('OPENSHIFT_POSTGRESQL_DB_PORT'):
	DB_PORT = os.environ['OPENSHIFT_POSTGRESQL_DB_PORT']


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sghyv&fc*%u25l_=&=0latcdx3)2r!t2=0du!98r!rtk4w&zgz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost', 'step-up-mountains.herokuapp.com']

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stepupmountains',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myproject.urls'

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
	ON_OPENSHIFT = True
if os.environ.has_key('OPENSHIFT_APP_NAME'):
	DB_NAME = os.environ['OPENSHIFT_APP_NAME']
if os.environ.has_key('OPENSHIFT_POSTGRESQL_DB_USERNAME'):
	DB_USER = os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME']
if os.environ.has_key('OPENSHIFT_POSTGRESQL_DB_PASSWORD'):
	DB_PASSWD = os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD']
if os.environ.has_key('OPENSHIFT_POSTGRESQL_DB_HOST'):
	DB_HOST = os.environ['OPENSHIFT_POSTGRESQL_DB_HOST']
if os.environ.has_key('OPENSHIFT_POSTGRESQL_DB_PORT'):
	DB_PORT = os.environ['OPENSHIFT_POSTGRESQL_DB_PORT']

if ON_OPENSHIFT:
	DATABASES = {
    	'default': {
        	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        	'NAME': 'stepupmountains',
        	'USER': os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],
        	'PASSWORD': os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],
        	'HOST': os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'],
        	'PORT': os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'],
    	}
	}
else:
	DATABASES = {
    	'default': {
        	'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
    	}
	}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

LOGIN_URL = '/'

import sys
if ON_OPENSHIFT:
	path = "app-root/repo/"
else:
	path = ""

#sys.path.append(os.path.join(os.getcwd(), path, "stepupmountains/manageobjects/"))
#sys.path.append(os.path.join(os.getcwd(), path, "stepupmountains/manageobjects/accounts/"))

DATETIME_FORMAT = 'Y-m-d H:i'
USE_L10N = False
LOGIN_URL = 'stepupmountains:accounts:django.contrib.auth.views.login'
LOGIN_REDIRECT_URL = '/'
#if DEBUG:
	#from pprint import pprint as p
	#print p(sys.path)

import dj_database_url
db_from_env = dj_database_url.config()
if db_from_env:
    DATABASES['default'].update(db_from_env)
