# coding: utf-8

import pytest
from flask_script import Manager
from hungry_mg import create_app

app = create_app()
manager = Manager(app, with_default_commands=False)


@manager.command
def test():
    """Runs the tests."""
    pytest.main(['-s', 'hungry_mg/tests'])


if __name__ == '__main__':
    manager.run()
