# TODO: There's no error handling whatsoever, as yet
"""
Utility functions for interacting with our Git repos
"""
from spamsub import app
import datetime
import json
from sqlalchemy import func
from models import *
from git import Repo
import requests
import os

basename = os.path.dirname(__file__)
now = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")

def ok_to_update():
    """ If we've got more than two new addresses, or a day's gone by """
    counter = Counter.query.first()
    elapsed = counter.timestamp - datetime.datetime.now()
    return any([counter.count >= 2, elapsed.days >= 1])

def check_if_exists(address):
    """
    Check whether a submitted address exists in the DB, add it if not,
    re-generate the spammers.txt file, and open a pull request with the updates
    """
    normalised = address.lower().strip()
    # add any missing spammers to our DB
    update_db()
    if not Address.query.filter_by(address=normalised).first():
        to_add = Address(address=normalised)
        db.session.add(to_add)
        count = Counter.query.first()
        count.count += 1
        db.session.add(count)
        db.session.commit()
        write_new_spammers()
        return False
    return True

def write_new_spammers():
    """ Synchronise all changes between GitHub and webapp """
    if ok_to_update():
        # re-generate spammers.txt
        with open(os.path.join(basename, "git_dir", 'spammers.txt'), 'w') as f:
            updated_spammers = " OR \n".join([addr.address for
                addr in Address.query.order_by('address').all()])
            f.write(updated_spammers)
            # files under version control should end with a newline
            f.write(" \n")
        # add spammers.txt to local repo
        index = repo.index
        index.add(['spammers.txt'])
        commit = index.commit("Updating Spammers on %s" % now)
        # push local repo to webapp's remote
        our_remote = repo.remotes.our_remote
        our_remote.push('master')
        # send pull request to main remote
        our_sha = "urschrei:master"
        their_sha = 'master'
        pull_request(our_sha, their_sha)
        # reset counter to 0
        counter = Counter.query.first()
        counter.count = 0
        counter.timestamp = func.now()
        db.session.add(counter)
        db.session.commit()

def get_spammers():
    """ Return an up-to-date list of spammers from the main repo text file """
    with open(os.path.join(basename, "git_dir", 'spammers.txt'), 'r') as f:
        spammers = f.readlines()
    # trim the " OR" and final newline from the entries
    # FIXME: this is a bit fragile
    return [spammer.split()[0] for spammer in spammers]

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

def checkout():
    """ Check out the latest version of spammers.txt from the main repo """
    repo = Repo(os.path.join(basename, "git_dir"))
    git = repo.git
    origin = repo.remotes.origin
    origin.pull('master')
    # make sure our file is the correct, clean version
    git.checkout("spammers.txt")

def update_db():
    """ Add any missing spammers to our app DB """
    # pull changes from main remote into local
    checkout()
    their_spammers = set(get_spammers())
    our_spammers = set(addr.address.strip() for addr in
        Address.query.order_by('address').all())
    to_update = [Address(address=new_addr) for new_addr in
        list(their_spammers - our_spammers)]
    db.session.add_all(to_update)
    db.session.commit()
