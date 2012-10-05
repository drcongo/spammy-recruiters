# no debugging by default - this is overriden in run.py for local dev
DEBUG = False
# production DB
SQLALCHEMY_DATABASE_URI = 'postgresql://spamsub:@localhost/spamsub'
