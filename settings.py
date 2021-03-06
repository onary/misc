"""
Django settings for core project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

IS_LOCAL_ENV = os.environ.has_key('IS_LOCAL_ENV')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xe@fsun!scz$rp%551!drm46=lzu7_zr%^-o$m84fl(j7wixgz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'paypal.standard',
    'paypal.pro',

    'apps.main',
    'apps.instascribe',
    'apps.paypalpro',
    "apps.middleware",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'apps.middleware.ssl.SSLRedirect',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if IS_LOCAL_ENV:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "geezer",
            "USER": "tomas",
            "PASSWORD": "11",
            "HOST": "",
            "PORT": "",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "d46jpkkf39otll",
            "USER": "pxwbibmwrdestv",
            "PASSWORD": "Wgwpw_LUEAvC4QOuGiSqcMfAB5",
            "HOST": "ec2-54-225-101-64.compute-1.amazonaws.com",
            "PORT": "5432",
            }
    }
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = ''

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "static"),
)


STATIC_URL = '/static/'

if IS_LOCAL_ENV:
    SITE_URL = 'http://127.0.0.1:8000'
    ENABLE_SSL = False
else:
    SITE_URL = 'http://misc-for-test.herokuapp.com'
    ENABLE_SSL = True

PAYPAL_TEST = True
PAYPAL_WPP_USER = "business.abraham_api1.gmail.com"
PAYPAL_WPP_PASSWORD = "1396126173"
PAYPAL_WPP_SIGNATURE = "AREmlapucenpmUBDAYOvRlPJS5DkA3OWPtFHRm.aFI2kqYhbNlAoxcko"

PAYPAL_RECEIVER_EMAIL = ""
PAYPAL_IDENTITY_TOKEN = ""
