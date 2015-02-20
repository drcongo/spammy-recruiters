#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from flask import *
from __init__ import app

from flask.ext.sqlalchemy import SQLAlchemy
from apps.spamsub.models import *

app.testing = True
client = app.test_client()
ctx = app.test_request_context()
ctx.push()
print "app and db have been imported.\nYou have a test client: client,\nand a test request context: ctx"
