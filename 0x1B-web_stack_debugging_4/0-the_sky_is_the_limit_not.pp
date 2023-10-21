# Enhancing the capability of the Nginx server to manage more traffic

# Adjusting the ULIMIT in the default nginx file
exec { 'modify-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/bin/:/usr/sbin/:/bin/'
}

# Relaunching Nginx
~> exec { 'restart-nginx-service':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
