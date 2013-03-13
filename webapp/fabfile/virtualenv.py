from fabric.decorators import task
from fabric.context_managers import settings, hide
from fabric.colors import cyan, red
from fabric.utils import abort
from utils import do


def build():
    """ Build or update the virtualenv """
    with settings(hide('stdout')):
        print(cyan('\nUpdating venv, installing packages...'))
        # remove non-virtualenv Fabric, because it causes problems
        # TODO: the logic of this will need to be re-thought
        do('sudo pip uninstall Fabric -qy', capture=True)
        do('[ -e venv ] || virtualenv venv --no-site-packages')
        # annoyingly, pip prints errors to stdout (instead of stderr), so we
        # have to check the return code and output only if there's an error.
        with settings(warn_only=True):
            # upgrade pip so we can take advantage of fancy new features
            pupgrade = do('venv/bin/pip install pip --upgrade')
            if pupgrade.failed:
                print(red(pupgrade))
                abort("pip upgrade unsuccessful %i" % pupgrade.return_code)
            # http://www.pip-installer.org/en/latest/cookbook.html#fast-local-installs
            do('mkdir -p pyarchives', capture=True)
            do('venv/bin/pip install --download pyarchives -r requirements.txt')
            pip = do(
                'venv/bin/pip install --no-index --find-links=file://vagrant/pyarchives -r requirements.txt --upgrade',
                capture=True)
        if pip.failed:
            print(red(pip))
            abort("pip exited with return code %i" % pip.return_code)
