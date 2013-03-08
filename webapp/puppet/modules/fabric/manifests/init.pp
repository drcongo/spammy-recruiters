class fabric {
  package { 'Fabric':
    provider => 'pip',
    ensure   => 'present',
  }
}