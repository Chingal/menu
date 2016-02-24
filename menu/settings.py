# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from django.core.urlresolvers import reverse_lazy

LOGIN_URL          = reverse_lazy('index')
LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGOUT_URL         = reverse_lazy('logout')


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6)_l$bkquhtlqoaz)u*2fz&ca_cum@h3zn^l+l+y3n)4h_zm=q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Aplicaciones de Django instaladas
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# Aplicaciones de terceros instaladas
THIRD_PARTY_APPS = (
    'south',
)

# Aplicaciones locales intaladas
LOCAL_APPS = (
    'inicio.apps.init',
)

# Aplicaciones instaladas
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'inicio.urls'

WSGI_APPLICATION = 'inicio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'inicio/media')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'inicio/static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'inicio/templates')
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'inicio.apis.context_processors.inicio',
)