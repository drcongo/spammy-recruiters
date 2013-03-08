from fabric.api import env
from fabric.decorators import task
from fabric.colors import cyan
from utils import do

@task
def check():
    """Syntax check on Puppet config."""
    print(cyan('\nChecking puppet syntax...'))
    do('find puppet -type f -name \'*.pp\' |xargs puppet parser validate')

@task
def apply():
    """Apply Puppet manifest."""
    print(cyan('\nApplying puppet manifest...'))
    do('sudo puppet apply --modulepath=puppet/modules/ puppet/manifests/standalone.pp' % env)
