import os
from fabric.decorators import task
from fabric.context_managers import settings, hide
from fabric.colors import cyan
from utils import do
from __init__ import upgrade_db


config_file_path = 'db/alembic.ini'


def build():
    """Initialise and migrate database to latest version."""
    if not os.path.exists(config_file_path):
        with virtualenv("venv"):
            print(cyan('\nUpdating database...'))
            with settings(hide('warnings'), warn_only=True):
                do('alembic -c %s init db/postgresql' % config_file_path)
                upgrade_db

