# Puppet manifest to fix Apache 500 error
$file_path = '/var/www/html/wp-settings.php'

file_line { 'replace_line':
  path    => $file_path,
  line    => '    define(\'DB_CHARSET\', \'utf8\');',
  match   => '    define(\'DB_CHARSET\', \'utf-8\');',
  ensure  => present,
}
