from .base import *
import os

# Disable debug mode

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    ('Ferdy Rodriguez', 'ferdyrodriguez@gmail.com'),
)

MANAGERS = ADMINS


EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = os.environ["NLB_EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["NLB_EMAIL_HOST_PASSWORD"]
DEFAULT_FROM_EMAIL = os.environ["NLB_EMAIL_ADDRESS"]
SERVER_EMAIL = os.environ["NLB_EMAIL_ADDRESS"]



# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE

COMPRESS_OFFLINE = True
COMPRESS_ENABLED = True
COMPRESS_URL = STATIC_URL
COMPRESS_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


# Send notification emails as a background task using Celery,
# to prevent this from blocking web server threads
# (requires the django-celery package):
# http://celery.readthedocs.org/en/latest/configuration.html

# import djcelery
#
# djcelery.setup_loader()
#
# CELERY_SEND_TASK_ERROR_EMAILS = True
# BROKER_URL = 'redis://'


# Use Redis as the cache backend for extra performance
# (requires the django-redis-cache package):
# http://wagtail.readthedocs.org/en/latest/howto/performance.html#cache

# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.cache.RedisCache',
#         'LOCATION': '127.0.0.1:6379',
#         'KEY_PREFIX': 'nancyblog',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
#         }
#     }
# }


try:
    from .local import *
except ImportError:
    pass
