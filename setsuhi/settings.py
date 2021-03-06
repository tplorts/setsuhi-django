"""
Django settings for setsuhi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



S3_SERVER_URL = "http://s3-ap-northeast-1.amazonaws.com/"
S3_BUCKET_NAME = "setsuhi-tokyo"
S3_BUCKET_URL = S3_SERVER_URL + S3_BUCKET_NAME + "/"
S3_STATIC_URL = S3_BUCKET_URL + "static/"


ML_COOKIE_NAME = "ml-language-selection"
ML_CONTEXT_KEY = "ml_active_language"
ML_DEFAULT_LANGUAGE = "ja"

languages = ['ja', 'en']


# Automatically detect whether this is running on my development
# computer, otherwise assuming that the environment is production.
isProduction = False
try:
    open('.dev')
except IOError:
    isProduction = True


SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')


DEBUG = not isProduction
TEMPLATE_DEBUG = not isProduction


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'email_obfuscator',
    'chosen',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'setsuhi.urls'

WSGI_APPLICATION = 'setsuhi.wsgi.application'



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Email settings
# Used for sending Setsuhi an email message when people
# fill out the inquiry form.
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'setsuhi.inquiries@gmail.com'
EMAIL_HOST_PASSWORD = 'shoD0-ka'
EMAIL_PORT = 587


##########
# HEROKU #
##########

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(),
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
if isProduction:
    STATIC_URL = S3_STATIC_URL
else:
    STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
