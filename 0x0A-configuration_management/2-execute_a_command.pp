# this manifest kills a process called killmenow
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/bin:/usr/bin:/usr/local/bin',
  onlyif  => 'pgrep -f killmenow',
}
