#puppet manifester for execution

exec { 'kill_process':
  command => 'pkill killmenow',
  path    => '/usr/bin:/bin',
}
