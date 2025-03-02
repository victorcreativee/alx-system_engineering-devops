# puppet code that fix a wordpress site 5xx error to 200 ok
# editing the mistyped .phpp

exec { 'fix-wordpress-server-error':
  command => '/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  onlyif  => '/bin/test -f /var/www/html/wp-settings.php',
}
