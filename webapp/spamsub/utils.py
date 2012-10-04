# TODO: There's no error handling whatsoever, as yet
"""
Utility functions for interacting with our Git repos
"""
from spamsub import app
import datetime
import json
from sqlalchemy.orm.exc import NoResultFound
from models import *
from git import Repo
import requests
import os

basename = os.path.dirname(__file__)
now = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")


def check_if_exists(address):
    """
    Check whether a submitted address exists in the DB, add it if not,
    re-generate the spammers.txt file, and open a pull request with the updates
    """
    normalised = address.lower().trim()
    try:
        _ = Address.query.filter_by(address=normalised).one()
    except NoResultFound:
        to_add = Address(address=normalised)
        db.session.add(to_add)
        db.session.commit()
        write_new_spammers()
        return False
    return True

def write_new_spammers():
    """ Synchronise all changes between Github and webapp """
    # pull changes from main remote into local
    repo = Repo(os.path.join(basename, "git_dir"))
    origin = repo.remotes.origin
    origin.pull('master')
    their_spammers = set(get_spammers())
    # add any missing spammers to our DB
    our_spammers = set([addr.address for addr in 
        Address.query.order_by('address').all()])
    to_update = [Address(address=new_addr) for new_addr in
        list(their_spammers - our_spammers)]
    db.session.add_all(to_update)
    db.session.commit()
    # re-generate spammers.txt
    with open(os.path.join(basename, "git_dir", 'spammers.txt'), 'w') as f:
        updated_spammers = " OR \n".join([addr.address for
            addr in Address.query.order_by('address').all()])
        f.write(updated_spammers)
        # files under version control should end with a newline
        f.write(" \n")
    # add spammers.txt to local repo and commit
    index = repo.index
    their_sha = repo.head.commit.hexsha
    index.add(['spammers.txt'])
    commit = index.commit("Updating Spammers on %s" % now)
    our_sha = repo.head.commit.hexsha
    # push local repo to webapp's remote
    our_remote = repo.remotes.our_remote
    our_remote.push('master')
    # send pull request to main remote
    pull_request(our_sha, their_sha)

def get_spammers():
    """ Return an up-to-date list of spammers from the main repo text file """
    with open(os.path.join(basename, "git_dir", 'spammers.txt'), 'r') as f:
        spammers = f.readlines()
    # trim the " OR" and final newline from the entries
    # FIXME: this is a bit fragile
    cleaned = list()
    for spammer in spammers:
        if spammer[-4:] == "OR \n":
            cleaned.append(spammer[:-5])
        else:
            cleaned.append(spammer[:-1])
    return cleaned

def pull_request(our_sha, their_sha):
    """ Open a pull request on the main repo """
    payload = {
        "title": "Updated Spammers on %s" % now,
        "body": "Updates from the webapp",
        "head": our_sha,
        "base": their_sha
    }
    headers = {
        "Authorization": 'token %s' % app.config['GITHUB_TOKEN'],
    }
    return requests.post(
        "https://api.github.com/repos/drcongo/spammy-recruiters/pulls",
        data=json.dumps(payload), headers=headers)
