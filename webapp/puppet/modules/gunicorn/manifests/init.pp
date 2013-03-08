# gunicorn is installed by the application
class gunicorn {
  file { '/etc/init/gunicorn.conf':
    ensure => present,
    source => 'puppet:///modules/gunicorn/gunicorn.conf',
  }
}