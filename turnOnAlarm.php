<?php
$pin = $_GET['pin'];
$comando = "echo raspberry | sudo -S python /var/www/html/scripts/onAlarm.py ".$pin;
system($comando);
?>
