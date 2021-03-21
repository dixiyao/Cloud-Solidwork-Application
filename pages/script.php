<?php
$action=$_GET['action'];
if $action=='login_check'{
	$userid=$_GET['userid'];
	exec("python3 /root/utils/login_check.py $userid");
}
?>