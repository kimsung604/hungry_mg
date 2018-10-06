# coding: utf-8

from contextlib import contextmanager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from flask_migrate import Migrate
from . import settings, helpers


def make_app():
    app = Flask(settings.APP_NAME,
                template_folder=settings.TEMPLATE_DIR,
                static_folder=settings.STATIC_DIR)

    app.config.from_object(settings.APP_CONF)

    return app


class Cache(object):
    def __init__(self, app=None, key=None):
        self.key = key or 'default'

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        try:
            import redis
        except ImportError:
            raise RuntimeError('no redis module found')

        conf = app.config.get('REDIS', None)

        if conf is None:
            raise ValueError('Neither REDIS is set.')

        if self.key not in conf:
            raise KeyError(f'not found {self.key} key in REDIS')

        self._client = redis.Redis(**conf[self.key])

    def __getattr__(self, attr):
        return getattr(self._client, attr)


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self, raise_error=True):
        try:
            yield
            self.session.commit()
        except BaseException as e:
            self.session.rollback()
            if raise_error:
                raise e


class LoadModule(object):
    def __init__(self, app=None, with_default_loads=False, **kwargs):
        self.app = app or make_app()
        self.extra = kwargs

        if with_default_loads:
            self.loads()

    def loads(self):
        if 'views' in self.extra:
            self.load_views()

        if 'db' in self.extra:
            self.load_models(self.extra['db'], settings.APP_VIEWS)

        if 'cache' in self.extra:
            self.load_caches(self.extra['cache'])

    def load_views(self, package=None):
        package = package or settings.APP_VIEWS
        helpers.register_blueprints(self.app, package)

    def load_models(self, db=None, package=None):
        if db is None:
            raise ValueError('db parameter is not be None')

        if isinstance(db, SQLAlchemy):
            package = package or settings.APP_MODELS
            # load models
            helpers.import_string(package)

            # init db
            db.init_app(self.app)

            # migrate
            Migrate(self.app, db)

    def load_caches(self, caches: list):
        for item in caches:
            if isinstance(item, Cache):
                item.init_app(self.app)
