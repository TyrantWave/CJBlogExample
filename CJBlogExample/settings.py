# Django settings for apolloblog project.
DEBUG = True

ADMINS = (
    ('Chris Johns', 'tyrantwave@gmail.com'),
)

MANAGERS = ADMINS

import os

# Running in development, so use localhost
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'blogdb',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'ApolloCJ'
    }
}

ALLOWED_HOSTS = ['localhost']  # List of allowed App Engine hosts when connecting from live site

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-GB'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = False

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'u#j0yr=_jwc1nc!top4a0+%)4$-ul64-=mxrnr6(n-90py8vr@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'CJBlogExample.urls'

TEMPLATE_DIRS = (
)

INSTALLED_APPS = (

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangotoolbox',
    'blog',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
