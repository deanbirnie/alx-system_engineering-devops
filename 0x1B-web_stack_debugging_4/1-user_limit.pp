# Configuration to allow user 'holberton' enhanced file access capability

# Modify the hard file limit for the 'holberton' user
exec { 'adjust-hard-limit-holberton':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/bin/:/usr/sbin/:/bin/'
}

# Modify the soft file limit for the 'holberton' user
exec { 'adjust-soft-limit-holberton':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/bin/:/usr/sbin/:/bin/'
}
