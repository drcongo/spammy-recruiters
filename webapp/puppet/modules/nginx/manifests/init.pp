class nginx {
  package { 'nginx':
    ensure => installed,
  }
  # Disable default nginx site
  file { '/etc/nginx/sites-enabled/default':
    ensure => absent,
    before => Service[nginx]
  }
  service { 'nginx':
    ensure => running,
  }
}

define nginx::site( $config = $name ) {
  file { "/etc/nginx/sites-enabled/${config}":
    ensure  => present,
    owner   => root,
    group   => root,
    mode    => '644',
    content => template("nginx/${config}.tpl"),
    require => Package[nginx],
    notify  => Service[nginx],
  }
}
