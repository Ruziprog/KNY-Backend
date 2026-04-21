from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'test_db.sqlite3',
    }
}

MIDDLEWARE = [m for m in MIDDLEWARE if 'whitenoise' not in m]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

SECRET_KEY = 'ci-test-key-not-for-production'