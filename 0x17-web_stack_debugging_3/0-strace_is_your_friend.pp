# Puppet manifest to resolve Apache 500 Internal Server Error
$target_file = '/var/www/html/wp-settings.php'

exec { 'edit_php_line':
  command => "sed -i 's/phpp/php/g' ${target_file}",
  path    => ['/bin', '/usr/bin']
}