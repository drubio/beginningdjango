# Django settings for coffeehouse project.

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = '%ea)cjy@v9(#7!b#(#20gl+4-6iur28dy=tc4f$-zbm-v#=!#t'

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'coffeehouse.about',
    'coffeehouse.stores',
    'coffeehouse.drinks',
    'django.contrib.admindocs',
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

ROOT_URLCONF = 'coffeehouse.urls'

WSGI_APPLICATION = 'coffeehouse.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

TEMPLATE_DIRS = ('%s/templates/'% (PROJECT_DIR),)

TEMPLATE_CONTEXT_PROCESSORS = ('coffeehouse.stores.processors.onsale',
                               'django.contrib.auth.context_processors.auth', 
                               'django.core.context_processors.debug', 
                               'django.core.context_processors.i18n', 
                               'django.core.context_processors.media', 
                               'django.core.context_processors.static', 
                               'django.core.context_processors.tz',
                               'django.contrib.messages.context_processors.messages',
                               'django.core.context_processors.request',)
INTERNAL_IPS = ('127.0.0.1')

STATICFILES_DIRS = ('%s/website-static-default/'% (BASE_DIR),
                    ('bootstrap','%s/bootstrap-3.1.1-dist/'% (BASE_DIR)),
                    ('jquery','%s/jquery-1-11-1-dist/'% (BASE_DIR)),
                    ('jquery-ui','%s/jquery-ui-1.10.4/'% (BASE_DIR)),)

STATIC_ROOT = '%s/coffeestatic/'% (BASE_DIR)
