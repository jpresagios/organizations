"""
Production Configurations

- Use WhiteNoise for serving static files
"""

from .base import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=False)

INTERNAL_IPS = ('127.0.0.1',)

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Use Whitenoise to serve static files
# See: https://whitenoise.readthedocs.io/
WHITENOISE_MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware', ]
MIDDLEWARE = WHITENOISE_MIDDLEWARE + MIDDLEWARE

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default=']HD]8U)IBBv;^Ctm~+H6LN(T4}7f}ewP$.d;4V0o(5/]a#fgK3')

INSTALLED_APPS += ['gunicorn', ]

# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['*', ])
# END SITE CONFIGURATION


# Static Assets
# ------------------------
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'