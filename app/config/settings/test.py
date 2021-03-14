# -*- coding: utf-8 -*-
"""
Test settings

- Used to run tests fast on the continuous integration server and locally
"""

from .common import *  # noqa

DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = False

SECRET_KEY = 'CHANGEME'

INSTALLED_APPS += ('django_nose',)

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

# Keep templates in memory so tests run faster
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]
