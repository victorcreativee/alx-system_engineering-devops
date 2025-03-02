# puppet code that fix a wordpress site 5xx error to 200 ok
# editing the mistyped .phpp

exec { 'fix-wordpress-server-error':
	command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	path => '/usr/bin/:/bin/',
}
