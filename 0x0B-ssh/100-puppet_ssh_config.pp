#!/usr/bin/env bash
# make changes to our configuration file using puppet

file_line { ' refuse to authenticate using a password':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  ensure => present,
}

file_line { 'use the private key':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  ensure => present,
}

