# coding: utf-8

from .factory import SQLAlchemy, Cache

# db
db = SQLAlchemy()

# cache
global_client = Cache()
CACHES = [
    global_client,
]
