# This puppet script sets up access to a server using only a public key and
# disables password authentication
file { '~/.ssh/config':
  ensure => file,
  owner  => 'root',
  mode   => '0600',
  content => "\
Host *
    IdentityFile ~/.ssh/school
    PreferredAuthentications publickey
    PasswordAuthentication no\n",
}
