from .base import *

DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG = True
TEMPLATE_DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
     'default':{
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME' : 'de2o9j0emnosgn',
    'USER' : 'kjuerftixrfohi',
    'PASSWORD' : 'UNdItjNXG60Kdn9TZgE0uzt3Fw',
    'HOST' : 'ec2-54-83-29-133.compute-1.amazonaws.com',
    'PORT' : '5432',
    }

}





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

#STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
#STATICFILES_DIRS=(BASE_DIR,'static')
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


#MEDIA_URL = '/media/'
#MEDIA_ROOT = BASE_DIR.child('media')

