# Django settings for coffeehouse project.

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = Path(__file__).resolve().parent

# Import socket to read host name
import socket
# If the host name starts with 'li', set LIVEHOST = True
if socket.gethostname().startswith('li'):
    LIVEHOST = True
else:
    LIVEHOST = False

# Define general behavior variables for live host and non-live host
if LIVEHOST:
    DEBUG = False
else:
    DEBUG = True

SECRET_KEY = 'django-insecure-3*w@re!%88p%w%+-3^g_z=pna5zot51cfjt4t^!6=u7sp7qo1!'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django_pdb',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'coffeehouse.about',
    'coffeehouse.stores',
    'coffeehouse.drinks',
    'raven.contrib.django.raven_compat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'coffeehouse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ PROJECT_DIR / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                               'coffeehouse.stores.processors.onsale',
                               'django.template.context_processors.debug',
                               'django.template.context_processors.request',
                               'django.contrib.auth.context_processors.auth',
                               'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'coffeehouse.wsgi.application'

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

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = ('127.0.0.1')

STATICFILES_DIRS = [ BASE_DIR / 'website-static-default',
                     ('bootstrap', BASE_DIR / 'bootstrap-5.0.2-dist'),
                     ('jquery', BASE_DIR / 'jquery-3-6-0-dist'),
                     ('jquery-ui', BASE_DIR / 'jquery-ui-1.13.1'),
                   ]

STATIC_ROOT = BASE_DIR / 'coffeestatic'

ADMINS = [('Webmaster', 'webmaster@coffeehouse.com'), ('Admin', 'admin@coffeehouse.com')]

RAVEN_CONFIG = {
    'dsn': 'https://<place_your_project_dsn_here>:<place_your_project_dsn_here>@sentry.io/151850',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    #'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
}


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
    'root': {
        'level': 'DEBUG',
        'handlers': ['sentry'],
    },    
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
        'sentry': {
            'level': 'DEBUG',
            'class': 'raven.contrib.django.handlers.SentryHandler',
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

