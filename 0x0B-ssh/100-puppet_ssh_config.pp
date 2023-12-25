#!/usr/bin/env bash
# make changes to our configuration file using puppet

file {
    path   => '/etc/.ssh/config',
    ensure => present,
    content => "
            Host *
            PasswordAuthentication no     
            IdentityFile ~/.ssh/school",
}
