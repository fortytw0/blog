from pathlib import Path
import os
import json

BASE_DIR = Path(__file__).resolve().parent.parent

from django.core.management.utils import get_random_secret_key
SECRET_KEY = get_random_secret_key()
DEBUG = os.environ.get('DEBUG', '1')=='1'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

from content.parser import parse_content, parse_tags
CONTENT_DIR = os.environ.get('CONTENT_DIR')
parse_tags(CONTENT_DIR)
parse_content(CONTENT_DIR, 'templates/blogs')



print("CWD : " , os.getcwd())
print("CLS : " , os.listdir("."))
print("Secret key : " , SECRET_KEY)
print("Debug : " , DEBUG)
print("Allowed hosts : " , ALLOWED_HOSTS)
print("Content Directory : " , CONTENT_DIR)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_ROOT = 'assets'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SITE_ID = 1
