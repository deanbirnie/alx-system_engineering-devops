# Fixes an issue with a specific Wordpress installtion

exec {'wp-settings-fix':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
  }
