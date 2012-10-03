# these settings are exported as SPAMSUB_CONFIGURATION by fabfile commands
# SPAMSUB_CONFIGURATION is then picked up by app/__init__.py

DEBUG = True
reloader = True
SQLALCHEMY_DATABASE_URI = 'postgresql://spamsub:@localhost/spamsub'
