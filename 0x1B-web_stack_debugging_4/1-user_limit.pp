# file_limits

# Increase ulimit parameters.
exec { 'set_file_limits':
  command => '/bin/bash -c "echo -e \'holberton hard nofile 65535\nholberton soft nofile 65535\' >> /etc/security/limits.conf"',
  unless  => '/bin/grep -E "^holberton[[:space:]]+nofile[[:space:]]+65535" /etc/security/limits.conf',
}
