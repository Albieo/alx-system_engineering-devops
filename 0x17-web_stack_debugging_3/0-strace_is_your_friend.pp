# Fix: typo in php file - from "phpp" to "php".

exec{ 'fixer-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
