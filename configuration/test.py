"""Test settings and globals which allow us to run the test suite locally"""

from .settings import *

# use sqlite in-memory for tests (faster)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
     },
}

# in testing mode
TESTING_MODE = True

WSGI_APPLICATION = 'configuration.wsgi.wsgi_test.application'

# implement dummy cache interface
CACHES = {
    "default" : {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        }
}
