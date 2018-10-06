# coding: utf-8


def create_app():
    from .factory import make_app, LoadModule
    from .core import db, CACHES

    app = make_app()

    LoadModule(app, with_default_loads=True, **{
        'views': True,
        'db': db,
        'cache': CACHES,
    })

    return app
