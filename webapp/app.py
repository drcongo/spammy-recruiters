#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" main site """

import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment, Bundle
from webassets.loaders import YAMLLoader
import locale
import logging


# set our locale data from the POSIX variable
locale.setlocale(locale.LC_ALL, '')

app = Flask(__name__)
# attach DB
from apps.shared.models import db
db.init_app(app)

# load configs
app.config.from_pyfile('config/common.py')
# actual CSRF secret key and github token go in here
try:
    app.config.from_pyfile('config/sensitive.py')
except IOError:
    pass
if os.getenv('DEV_CONFIGURATION'):
    app.config.from_envvar('DEV_CONFIGURATION')

# attach assets
assets = Environment(app)
assets.versions = 'hash'
assets.url = app.static_url_path
manifest_path = os.path.realpath(
    os.path.join(os.path.dirname(__file__), '.static-manifest'))
assets.manifest = 'file://%s' % manifest_path
bundles = YAMLLoader(os.path.realpath(
    os.path.join(os.path.dirname(__file__), 'assets.yml'))).load_bundles()
for bundle_name, bundle in bundles.items():
    assets.register(bundle_name, bundle)

## import blueprint(s), and attach
from apps.spamsub.views import spamsub
app.register_blueprint(spamsub, url_prefix='/')

# set up logging
# the following line causes a crash using logging 0.4.9.6
# Function:           %(funcName)s
if not app.debug:
    log_format = logging.Formatter("""
---
Message type:       %(levelname)s
Location:           %(pathname)s:%(lineno)d
Module:             %(module)s
Time:               %(asctime)s

%(message)s

""")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_format)
    app.logger.addHandler(stream_handler)


# set up error handling pages
@app.errorhandler(404)
def page_not_found(error):
    """ 404 handler """
    return render_template(
        'errors/404.jinja'), 404


@app.errorhandler(500)
def application_error(error):
    """ 500 handler """
    return render_template(
        'errors/500.jinja'), 500
