# Puppet manifest to adjust file limits for the specified user

# Step 1: Increase the hard file limit for the user
exec { 'increase_hard_file_limit':
  command => 'sed -i "/USERNAME hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

# Step 2: Increase the soft file limit for the user
exec { 'increase_soft_file_limit':
  command => 'sed -i "/USERNAME soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
