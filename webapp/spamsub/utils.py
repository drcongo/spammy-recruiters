"""
Utility functions for interacting with our Git repos
"""
from sqlalchemy.orm.exc import NoResultFound
from models import *
# http://packages.python.org/GitPython/0.3.2/tutorial.html#the-index-object

def check_if_exists(address):
    """ Check whether a submitted address exists in the DB, add it if not """
    normalised = address.lower()
    try:
        _ = Address.query.filter_by(address=normalised).one()
    except NoResultFound:
        to_add = Address(normalised)
        db.session.add(to_add)
        db.session.commit()
        return False
    return True

# pull from main repo
# push changes to app repo
# update DB with entries
# append new entries from DB to local copy of text file
# commit text file and push to app repo
# post pull request to main repo using GitHub API
