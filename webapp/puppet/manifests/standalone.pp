#
# Standalone manifest - for dev Vagrant box.
#

import 'lib/*.pp'

include stdlib
include fabric
include git
include gunicorn
include nginx
include postgresql::server
include python
include vagrant

nginx::site { 'gunicorn':
  config => 'gunicorn',
}
package { [ 'yui-compressor' ]:
  ensure => 'installed',
}
package {"alembic":
    ensure => "installed",
    provider => "pip"
}
# creates a blank db for our app to use
postgresql::db{ 'app_db':
  user          => 'flask_user',
  password      => 'flask_pass',
  grant         => 'all',
}
