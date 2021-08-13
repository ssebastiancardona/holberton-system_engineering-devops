# Terminator de porcesos T-800
exec { 'killmenow':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
}