#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append("..")
from flask import *
from webapp import app, db
from webapp.apps.spamsub.models import *

app.testing = True
client = app.test_client()
ctx = app.test_request_context()
ctx.push()
print "app and db have been imported.\nYou have a test client: client,\nand a test request context: ctx"
