# coding: utf-8

import os

BASE_DIR = os.path.dirname(__file__)

TEMPLATE_DIR = os.path.join(BASE_DIR, 'public/templates')
STATIC_DIR = os.path.join(BASE_DIR, 'public/static')

APP_NAME = 'hungry_mg'
APP_CONF = f'{APP_NAME}.settings'
APP_VIEWS = f'{APP_NAME}.views'
APP_MODELS = f'{APP_NAME}.models'

DEBUG = True
SECRET_KEY = os.urandom(16)

# database
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_DATABASE_URI = 'mysql+pymyql://root:@127.0.0.1:3306/hungry?charset=utf8' # noqa
SQLALCHEMY_ECHO = DEBUG
SQLALCHEMY_TRACK_MODIFICATIONS = False

# cache
REDIS = {
    'default': {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 0,
    },
}

# celery
