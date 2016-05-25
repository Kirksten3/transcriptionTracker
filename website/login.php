<?php
    header('Content-Type: application/json');
	$success = FALSE;
	if (isset($_POST['name']) && isset($_POST['id'])) {
		//echo "FORM INFORMATION HAS BEEN SET. Username: " . $_POST['name'];
		//file has to be set to 666
		$file = fopen('user.txt', 'a+');
		$size = filesize('user.txt');
		fseek($file, $size);
		fwrite($file, $_POST['id'] . '&' . $_POST['name'] . PHP_EOL);
		fclose($file);
                
                $response = array('success' => 1, 'name' => $_POST['name']);
		echo json_encode($response);
                
		$success = TRUE;
	}
	if (isset($_POST['id']) && !isset($_POST['name'])) {
		$fileArray = file('user.txt');
		$len = count($fileArray);
		for ($i = 0; $i < $len; $i++) {
			if (strpos($fileArray[$i], $_POST['id']) !== FALSE) {
                                $user = explode('&', $fileArray[$i]);
                                //trim the newline character from the response
				$response = array('success' => 1, 'name' => trim($user[1]));
                                echo json_encode($response);
				$success = TRUE;
				break;
			}
		}
	}
	if (!$success){
		$response = array('success' => 0, 'name' => NULL);
	}
?>