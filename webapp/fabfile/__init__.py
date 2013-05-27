import sys
import os

from fabric.api import env, run, local, require, cd, put
from fabric.colors import cyan, yellow, green, red
from fabric.decorators import task
from alembic.config import Config
from alembic import command
import alembic_init
import puppet
import virtualenv

env.basename = os.path.dirname(__file__)

alembic_cfg = Config(os.path.join(
    os.path.dirname(env.basename),
    "db",
    "alembic.ini"))

alembic_cfg.set_main_option(
    "sqlalchemy.url", "postgresql://flask_user:flask_pass@localhost/app_db")


@task
def build():
    """Execute build tasks for all components."""
    virtualenv.build()
    alembic_init.build()


@task
def run_app():
    """
    Start app in debug mode with reloading turned on. Dev only
    """
    with cd(env.basename):
        # clean up any *.pyc files in our app dir
        local('export DEV_CONFIGURATION=`pwd`/config/dev.py && venv/bin/python ./run.py')


@task
def shell():
    """
    Run iPython without the deprecated Werkzeug stuff
    """
    with cd(env.basename):
        local('export DEV_CONFIGURATION=`pwd`/config/dev.py && venv/bin/ipython -i -c "%run shell.py"')


# Alembic stuff. See http://alembic.readthedocs.org/en/latest/api.html
@task
def revision(msg):
    """
    Create a new Migration
    """
    command.revision(alembic_cfg, message=msg)


@task
def upgrade_db(rev="head"):
    """
    Upgrade DB to specified revision or head
    """
    print(cyan("Running Alembic migrations, upgrading DB to %s" % rev))
    command.upgrade(alembic_cfg, rev)


@task
def downgrade_db(rev="base"):
    """
    Downgrade DB to specified revision or base
    """
    print(cyan("Running Alembic migrations, downgrading DB to %s" % rev))
    command.downgrade(alembic_cfg, rev)


@task
def show_migrations():
    """
    List all DB migrations in chronological order
    """
    command.history(alembic_cfg)
