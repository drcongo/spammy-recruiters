import os
import sys
from flask import *
from __init__ import app
from flask.ext.sqlalchemy import SQLAlchemy
# if you add blueprints, import their models as below
from apps.spamsub.models import *

app.testing = True
app.test_client()
ctx = app.test_request_context()
ctx.push()
print "app and db have been imported.\nYou have a test client: client,\nand a test request context: ctx"
