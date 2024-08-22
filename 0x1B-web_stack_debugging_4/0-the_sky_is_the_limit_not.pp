# Increase the traffic limit to fix failed request

# Increase on the ULIMIT of the default file.
exec { 'Nginx-fix':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Nginx restart.
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}
