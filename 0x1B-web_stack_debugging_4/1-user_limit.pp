# This Puppet script enables the holberton user to login and open files without encountering errors.

# Step 1: Increase the hard file limit for user holberton
exec { 'increase_hard_file_limit_for_holberton_user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

# Step 2: Increase the soft file limit for user holberton
exec { 'increase_soft_file_limit_for_holberton_user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
