#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from flask import *
from spamsub import app, db

from spamsub.models import *

app.testing = True
client = app.test_client()
ctx = app.test_request_context()
ctx.push()
print "app and db have been imported.\nYou have a test client: client,\nand a test request context: ctx"
