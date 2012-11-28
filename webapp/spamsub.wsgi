activate_this = '/full/path/to/virtualenv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys
sys.path.insert(0, "/full/path/to/webapp")

from webapp import app
application = app
