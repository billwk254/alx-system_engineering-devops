# Puppet manifest to install Flask version 2.1.0 and its dependencies using pip3

class { 'python::pip':
  version => 'latest',
}

package { 'python3-pip':
  ensure => installed,
}

exec { 'Install Flask 2.1.0':
  command     => 'pip3 install Flask==2.1.0',
  path        => '/usr/local/bin',
  refreshonly => true,
}

exec { 'Install werkzeug 2.1.1':
  command     => 'pip3 install werkzeug==2.1.1',
  path        => '/usr/local/bin',
  refreshonly => true,
}

