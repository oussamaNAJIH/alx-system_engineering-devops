# 2-execute_a_command.pp

exec { 'kill_process_killmenow':
  command     => 'pkill -f killmenow',
  refreshonly => true,
  provider  => 'shell',
}