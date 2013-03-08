from fabric.api import require, env, local, run as fab_run
from fabric.utils import abort
import config

def do(*args, **kwargs):
    """
    Runs command locally or remotely depending on whether a remote host has
    been specified.
    """
    if env.host_string:
        with settings(cd(config.remote_path)):
            return fab_run(*args, **kwargs)
    else:
        return local(*args, **kwargs)

def require_host():
    """
    Forces a remote host to be set, automatically detecting it from the current
    git branch if possible.
    """
    if not env.host_string:

        # Detect current branch from git, based on config
        branch = local('git symbolic-ref -q HEAD', capture=True).split('/')[2]

        # Ensure the current branch matches up to a known branch
        if branch in config.branches:
            env.branch = branch

        require('branch')

        # Manually set host_string variable
        env.host_string = env.branches[branch]['hosts']

    require('host_string')
