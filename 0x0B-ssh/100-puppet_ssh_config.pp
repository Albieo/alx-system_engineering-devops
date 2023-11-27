#!/usr/bin/env bash
# Client configuration file

file {'/etc/ssh/ssh_config':
  ensure => present,
}

file_line { 'Disable password':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^@PasswordAuthentication',
}

file_line { 'id file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^@IdentityFile',
}
