# -*- coding: utf-8 -*-
from flask.ext.testing import TestCase
from spamsub import app as ss
from spamsub import db
from spamsub.models import *

class MyTest(TestCase):
    """ TestCase Flask extension class """

    # Setup boilerplate methods and settings

    def create_app(self):

        app = ss
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
        app.config['CSRF_ENABLED'] = False
        return app

    def setUp(self):

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

    def test_address_exists(self):
        """ Passes if we get the "We already know about … though" message """ 
        response = self.client.post('/', data=dict(address='test-address.com'))
        assert 'though' in response.data

    def test_new_address(self):
        """ Passes if we add the POSTed address to the db """
        response = self.client.post('/', data=dict(address='new-address.com'))
        assert 'added' in response.data
