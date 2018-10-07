# hungry-mg
hungry

## Development Environment
At the bare minimum you'll need the following for your development environment
- [Python](http://www.python.org/)
- [MySQL](http://www.mysql.com/)
- [Redis](http://redis.io/)

It is strongly recommended to also install and use the following tools:
- [Pipenv](https://github.com/pypa/pipenv)

### Local Setup

#### 1. Install pipenv
    $ brew install pipenv
    
Pipenv Warning: the environment variable LANG is not set!)

    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8

Pipenv: Checking pip version (last version bug)

    $ pipenv run pip --version
    ...
    pip 18.1 from ..
If the pip version is 18.1, it will not work properly, so you need to re-install to version 18.0

    $ pipenv run pip install pip==18.0

#### 2. Clone the project
    $ git clone git@github.com:nadostar/hungry_mg.git hungry_mg
    cd hungry_mg

#### 3. Create and initialize virtualenv for the project
    $ pipenv sync

#### 4. Run the development server
    $ flask run