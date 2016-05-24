<?php
	$success = FALSE;
	if (isset($_POST['name']) && isset($_POST['id'])) {
		//echo "FORM INFORMATION HAS BEEN SET. Username: " . $_POST['name'];
		
		$file = fopen('user.txt', 'a+');
		$size = filesize('user.txt');
		fseek($file, $size);
		fwrite($file, $_POST['id'] . '&' . $_POST['name']);
		fclose($file);
		echo "Valid Register";
		$success = TRUE;
	}
	if (isset($_POST['id']) && !isset($_POST['name'])) {
		$fileArray = file('user.txt');
		$len = count($fileArray);
		for ($i = 0; $i < $len; $i++) {
			if (strpos($fileArray[$i], $_POST['id']) !== FALSE) {
				echo "Valid Login";
				$success = TRUE;
				break;
			}
		}
	}
	if (!$success){
		echo "Unable to Login / Register";
	}
?>