from .base import *

DEBUG = False

ADMINS = [
    ('username', 'email'),
]

ALLOWED_HOSTS = ['your_allowed.host']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True