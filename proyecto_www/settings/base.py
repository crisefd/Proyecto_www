from unipath import Path
import os

BASE_DIR = Path(__file__).ancestor(3)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')4j=2+73&ed9hsj0l4nb$!=(v1)w*xgn17p^e&zv=6nzh_%cvt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)


LOCAL_APPS = (
    'apps.home',
    'apps.inventario',
    'apps.usuarios',
    'apps.ordenes_trabajo',
    'apps.sucursales',
    'apps.ventas_cotizaciones',
)


THIRD_PARTY_APPS = (
    'corsheaders',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'proyecto_www.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'proyecto_www.wsgi.application'

STATIC_URL = '/static/'
STATICFILES_DIRS=(BASE_DIR,'static',)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
        'GET',
        'POST',
        'PUT',
        'PATCH',
        'DELETE',
        'OPTIONS',
    )




MODELO_SUCURSALES = 'sucursales.Sucursales'
AUTH_USER_MODEL = 'usuarios.User'
MODELO_AUTO = 'inventario.Automovil'
MODELO_REPUESTO = 'inventario.Repuesto'
MODELO_MECANICO = 'ordenes_trabajo.Mecanicos'
