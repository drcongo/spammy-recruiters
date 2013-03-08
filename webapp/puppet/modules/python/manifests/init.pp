class python {
  include python::modules
  package { 'python':
    ensure => installed,
  }
}
