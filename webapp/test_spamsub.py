# -*- coding: utf-8 -*-


import os
from flask.ext.testing import TestCase
from webapp import app as ss
from webapp import db
from webapp.apps.spamsub.models import *
from webapp.apps.spamsub import utils
from datetime import timedelta


def mock_checkout():
    """ lets just pretend we're checking out the right file """
    pass

def mock_pull_request():
    """ don't actually open a pull request """
    return True

utils.repo_checkout = mock_checkout
utils.pull_request = mock_pull_request



class MyTest(TestCase):
    """ TestCase Flask extension class """

    # Setup boilerplate methods and settings

    def create_app(self):

        app = ss
        app.config.from_pyfile(os.path.join(app.root_path, 'config/dev.py'))
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
        app.config['CSRF_ENABLED'] = False
        return app

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
        db.create_all()
        # add an initial timestamp, address, and update count
        db.session.add_all([
            UpdateCheck(),
            Address(address="@test-address.com"),
            Counter(count=0)
            ])
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()

    # Actual tests start here
    def test_exists(self):
        """ Should pass because we've added the address during setup """
        print Address.query.filter_by(address="@test-address.com").first().address
        assert utils.check_if_exists('test-address.com')
        print Address.query.filter_by(address="@test-address.com").first().address

    def test_address_exists(self):
        """ Passes if we get the "We already know about … though" message """
        response = self.client.post('/', data=dict(
            address='test-address.com',
            recaptcha_challenge_field='test',
            recaptcha_response_field='test'))
        assert 'though' in response.data

    def test_new_address(self):
        """ Passes if we add the POSTed address to the db """
        response = self.client.post('/', data=dict(
            address='new-address.com',
            recaptcha_challenge_field='test',
            recaptcha_response_field='test'))
        assert 'added' in response.data

    def test_ok_to_update_counter(self):
        """ Should pass because we have more than two new addresses """
        ctr = Counter.query.first()
        ctr.count += 2
        db.session.add(ctr)
        db.session.commit()
        assert utils.ok_to_update()

    def test_ok_to_update_date(self):
        """ Should pass because more than a day has passed """
        ctr = Counter.query.first()
        ctr.timestamp -= timedelta(days=1, seconds=1)
        db.session.add(ctr)
        db.session.commit()
        assert utils.ok_to_update()

    def test_ok_to_update_fails(self):
        """ Should fail because the counter's zero, and < 24 hours old """
        assert not utils.ok_to_update()


