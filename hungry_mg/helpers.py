# coding: utf-8

from werkzeug.utils import find_modules, import_string
from flask import Blueprint


def register_blueprints(app, package=None):
    if package is None:
        raise ValueError('package parameter not be None')

    for name in find_modules(package):
        mod = import_string(name)
        if hasattr(mod, 'app') and isinstance(mod.app, Blueprint):
            app.register_blueprint(mod.app)
