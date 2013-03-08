# no debugging by default - this is overriden in run.py for local dev
DEBUG = False
# production DB
SQLALCHEMY_DATABASE_URI = 'postgresql://flask_user:flask_pass@localhost/app_db'
# Generate your own secret key
SECRET_KEY = 'foo'
