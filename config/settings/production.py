from .base import *

secrets = json.loads(open(SECRET_PRODUCTION, 'rt').read())

DEBUG = False

ALLOWED_HOSTS = [
    '.elasticbeanstalk.com',
    '127.0.0.1',
    'localhost',
]

WSGI_APPLICATION = 'config.wsgi.production.application'
INSTALLED_APPS += [
    'storages',
]

set_config(secrets, module_name=__name__, start=True)

# # Media(user-uploaded file)을 위한 스토리지
# DEFAULT_FILE_STORAGE = 'config.storage.DefaultFileStorage'
# # Static files(collectstatic) 을 위한 스토리지
# STATICFILES_STORAGE = 'config.storage.StaticFileStorage'
