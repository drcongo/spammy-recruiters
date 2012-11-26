#!/usr/bin/env python
import sys

sys.path.append("..")

from webapp import app
app.run(host='0.0.0.0')