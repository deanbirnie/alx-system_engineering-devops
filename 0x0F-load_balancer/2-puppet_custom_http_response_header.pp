# Puppet manifest to configure a custom HTTP response header in Nginx

class nginx_custom_header {

  package { 'nginx':
    ensure => installed,
  }
  file { '/etc/nginx/conf.d/custom-header.conf':
    content => "server_tokens off;\nadd_header X-Served-By ${hostname};",
    ensure  => present,
    notify  => Service['nginx'],
  }
  service { 'nginx':
    ensure  => running,
    enable  => true,
  }
}

include nginx_custom_header
