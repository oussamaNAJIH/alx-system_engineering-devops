#!/usr/bin/env bash
# make changes to our configuration file using puppet

file {
    path   => 'ect/.ssh/config',
    ensure => present,
    content => "
            Host *
            PasswordAuthentication no     
            IdentityFile ~/.ssh/school",
}
