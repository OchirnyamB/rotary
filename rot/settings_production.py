from base_settings import *
from email import *
import site, os

DEBUG = False

#Fill this in with relevant DB info
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file
        'USER': '',                  # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

#venv site packages
site.addsitedir('')
#venv activate this
activate_this = os.path.expanduser("")
execfile(activate_this, dict(__file__=activate_this))

#static host
STATIC_ROOT = ""
#media host
MEDIA_ROOT = ""
STATIC_URL= "/static/"
MEDIA_URL= "/media/"

#remake this
SECRET_KEY = ""

#domain name
ALLOWED_HOSTS = []
