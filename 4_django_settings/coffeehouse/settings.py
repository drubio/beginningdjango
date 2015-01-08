# Django settings for coffeehouse project.

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Import socket to read host name
import socket
# If the host name starts with 'li', set LIVEHOST = True
if socket.gethostname().startswith('li'):
    LIVEHOST = True
else:
    LIVEHOST = False

# Define general behavior variables for live host and non live host
if LIVEHOST:
    DEBUG = False
    TEMPLATE_DEBUG = False
else:
    DEBUG = True
    TEMPLATE_DEBUG = True

SECRET_KEY = '%ea)cjy@v9(#7!b#(#20gl+4-6iur28dy=tc4f$-zbm-v#=!#t'

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

ADMINS =(('Webmaster', 'webmaster@coffeehouse.com'), ('Admin', 'admin@coffeehouse.com'))


if LIVEHOST:
    # Output to file based SMTP server on live host 
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = '/tmp/django-project-messages'

else: 
    # Output to console for non live host
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
	    'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
	    'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'development_logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': '/tmp/django_dev.log',
            'formatter': 'verbose'
        },
        'production_logfile': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': '/tmp/django_production.log',
            'formatter': 'simple'
        },
        'dba_logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_true','require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': '/tmp/django_dba.log',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'coffeehouse': {
            'handlers': ['console','development_logfile','production_logfile'],
         },
        'dba': {
            'handlers': ['console','dba_logfile'],
        },
        'django': {
            'handlers': ['console','development_logfile','production_logfile'],
        },
        'py.warnings': {
            'handlers': ['console','development_logfile'],
        },
    }
}
