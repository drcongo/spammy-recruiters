class python::modules {
  package { [ 'python-virtualenv', 'python-dev', ]:
    ensure => 'installed',
  }
}
