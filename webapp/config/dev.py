# these settings are exported as DEV_CONFIGURATION by fabfile commands
# DEV_CONFIGURATION is then picked up by app/__init__.py

DEBUG = True
reloader = True
SQLALCHEMY_DATABASE_URI = 'postgresql://flask_user:flask_pass@localhost/app_db'
# this won't be picked up when running under production
SECRET_KEY = '088e57ce8c4db3c89c014cf463685601e3a02292efed95f20860e31a0cb7f0fc2216e29e2bfab8a9b4e0cb4e508698ef931839e044182b5d0e500dfeeaa027df6686ebc233b1361189dfde2a618cd6ad9fea99b0f8062545c9e60005724a4cf10eafabeaef8468020dad52dc7ebbe0b10c5d0d915604c56fed35614ae7b75737'

RECAPTCHA_PUBLIC_KEY = "6LcogwITAAAAADF00rpMiI7cRd3-hdFw421ZlY7Z"
RECAPTCHA_PRIVATE_KEY = "6LcogwITAAAAAMOa89LJSAVgr00SUfSNMzmefgis"
RECAPTCHA_USE_SSL = False
RECAPTCHA_OPTIONS = {
    'tabindex': 1,
}
