"""
Django settings for mwd project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import re

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Retrieve production stage environment variable
class MissingEnvironmentVariable(Exception):
    pass

class InvalidEnvironmentVariable(Exception):
    pass

try:
    STAGE = os.environ['STAGE']
except KeyError:
    raise MissingEnvironmentVariable('Environment variable STAGE is not defined.')

# SECURITY WARNING: don't run with debug turned on in production!
if STAGE == 'development' or STAGE == 'staging':
    DEBUG = True
elif STAGE == 'production':
    DEBUG = False
else:
    raise InvalidEnvironmentVariable('The value of environment variable STAGE is not valid.')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY_FILE = '%s/auth/secret.txt' % BASE_DIR
with open(SECRET_KEY_FILE, 'r', encoding='utf8') as f:
    content = f.readline()
SECRET_KEY = content[:-1]

if STAGE == 'development':
    ALLOWED_HOSTS = [
        'localhost',
    ]
elif STAGE == 'staging':
    ALLOWED_HOSTS = [
        'staging.mccarthycode.com',
        'staging.mccarthywebdesign.com',
    ]
elif STAGE == 'production':
    ALLOWED_HOSTS = [
        'mccarthycode.com',
        'www.mccarthycode.com',
        'mccarthywebdesign.com',
        'www.mccarthywebdesign.com',
    ]


# Application definition

INSTALLED_APPS = [
    'home',
    'legal',
    'quotes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mwd.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'home.context_processors.stage',
                'home.context_processors.year',
                'home.context_processors.recaptcha_site_key',
            ],
        },
    },
]

WSGI_APPLICATION = 'mwd.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

PGPASSWORD_FILE = '%s/auth/.pgpass' % BASE_DIR
with open(PGPASSWORD_FILE, 'r', encoding='utf8') as f:
    content = f.readline()
PGPASSWORD = content[12:-1]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mwd',
        'USER': 'postgres',
        'PASSWORD': PGPASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


# Media files

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Project variables
PHONE_REGEX = re.compile(
    r'^(\+?1)?[\s\.-]?\(?(\d{3})\)?[\s\.-]?(\d{3})[\s\.-]?(\d{4})$'
)


# reCAPTCHA secret key
RECAPTCHA_FILE = '%s/auth/recaptcha.txt' % BASE_DIR
RECAPTCHA_V2_SECRET_KEY = RECAPTCHA_V3_SECRET_KEY = ''
with open(RECAPTCHA_FILE, 'r', encoding='utf8') as f:
    content = f.readline()
    RECAPTCHA_V2_SECRET_KEY = content[:-1]
    content = f.readline()
    RECAPTCHA_V3_SECRET_KEY = content[:-1]
