from fabric.decorators import task
from fabric.context_managers import settings, hide
from fabric.colors import cyan, red
from fabric.utils import abort
from utils import do

def build():
    """ Build or update the virtualenv """
    with settings(hide('stdout')):
        print(cyan('\nUpdating venv, installing packages...'))
        do('[ -e venv ] || virtualenv venv --no-site-packages')
        # annoyingly, pip prints errors to stdout (instead of stderr), so we
        # have to check the return code and output only if there's an error.
        with settings(warn_only=True):
            pip = do('venv/bin/pip install -r requirements.txt', capture=True)
            # remove non-virtualenv pip, because it causes problems
            # TODO: the logic of this will need to be re-thought
            remfab = do(
                'sudo pip uninstall Fabric -qy',
                capture=True)
        if pip.failed:
            print(red(pip))
            abort("pip exited with return code %i" % pip.return_code)
