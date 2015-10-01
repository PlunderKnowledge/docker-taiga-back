from .common import *

DATABASES = {
   'default': {
       'ENGINE': 'transaction_hooks.backends.postgresql_psycopg2',
       'NAME': '${DB_NAME}',
       'USER': '${DB_USER}',
       'PASSWORD': '${DB_PASS}',
       'HOST': '${DB_HOST}',
       'PORT': '${DB_PORT}',
   }
}

HOST = 'http://${HOSTNAME}/'

MEDIA_ROOT = '/usr/local/taiga/media'
MEDIA_URL = '${MEDIA_URL}'

STATIC_ROOT = '/usr/local/taiga/static'
STATIC_URL = '${STATIC_URL}'
ADMIN_MEDIA_PREFIX = '${STATIC_URL}admin/'

SITES["front"]["scheme"] = '${FRONT_SCHEME}'
SITES["front"]["domain"] = '${FRONT_DOMAIN}'
SITES["api"]["scheme"] = '${API_SCHEME}'
SITES["api"]["domain"] = '${API_DOMAIN}'

SECRET_KEY = '${SECRET_KEY}'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = ${EMAIL_USE_TLS}
EMAIL_HOST = '${EMAIL_HOST}'
EMAIL_PORT = ${EMAIL_PORT}
EMAIL_HOST_USER = '${EMAIL_HOST_USER}'
EMAIL_HOST_PASSWORD = '${EMAIL_HOST_PASSWORD}'

DEFAULT_FROM_EMAIL = '${DEFAULT_FROM_EMAIL}'

DEBUG = ${DEBUG}
TEMPLATE_DEBUG = ${TEMPLATE_DEBUG}
PUBLIC_REGISTER_ENABLED = ${PUBLIC_REGISTER_ENABLED}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = "UTC"

# FEEDBACK MODULE (See config in taiga-front too)
FEEDBACK_ENABLED = ${FEEDBACK_ENABLED}
FEEDBACK_EMAIL = '${FEEDBACK_EMAIL}'

# STATS MODULE
STATS_ENABLED = ${STATS_ENABLED}

# SITEMAP
FRONT_SITEMAP_ENABLED = ${FRONT_SITEMAP_ENABLED}

# Uncomment and populate with proper connection parameters
# for enable github login/singin.
GITHUB_API_CLIENT_ID = "yourgithubclientid"
GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"
