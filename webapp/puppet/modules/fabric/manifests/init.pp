class fabric {
  package { 'pip':
    provider => 'pip',
    ensure   => 'present',
  }
  package { 'Fabric':
    provider => 'pip',
    ensure   => 'present',
  }
}
