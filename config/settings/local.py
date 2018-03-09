from .base import *

secrets_base = json.loads(open(SECRET_LOCAL, 'rt').read())

DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.local.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
