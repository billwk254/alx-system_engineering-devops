# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Create custom Nginx configuration file
file { '/etc/nginx/conf.d/99-custom-header.conf':
  ensure  => 'file',
  content => "add_header X-Served-By ${hostname};\n",
  require => Package['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/conf.d/99-custom-header.conf'],
}
