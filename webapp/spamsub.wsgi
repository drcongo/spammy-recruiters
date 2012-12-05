import os
basename = os.path.dirname(__file__)
# the following line assumes a virtualenv dir 'venv' in this dir
activate_this = os.path.join(basename, 'venv/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
import sys
sys.path.insert(0, os.path.abspath(os.path.join(basename, "..")))

from webapp import app
application = app
