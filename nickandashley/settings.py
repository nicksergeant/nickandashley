# Django settings for nickandashley project.
import os.path, socket

DEBUG = False

BASE_PATH = os.path.dirname(__file__)

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Nick Sergeant', 'nick@nicksergeant.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nickandashley',
        'USER': 'nickandashley',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
MEDIA_ROOT = os.path.join(BASE_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.comhttps://nickandashley.s3.amazonaws.com/"
MEDIA_URL = 'https://nickandashley.s3.amazonaws.com/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.comhttps://nickandashley.s3.amazonaws.com/", "https://nickandashley.s3.amazonaws.com/".
ADMIN_MEDIA_PREFIX = 'https://nickandashley.s3.amazonaws.com/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'nickandashley.urls'

TEMPLATE_DIRS = os.path.join(BASE_PATH, 'templates')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'nickandashley.guestbook',
    'nickandashley.guests',
    'nickandashley.contacts',
    'compressor',
    'gunicorn',
)

COMPRESS_OUTPUT_DIR = "cache"
COMPRESS = True

if DEBUG:
    INSTALLED_APPS += ('django_extensions',)
