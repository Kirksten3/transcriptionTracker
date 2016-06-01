<?php
/*
 * File Helper class for reading users / data from server
 */
 
class FileHelper
{
	public static function CleanArray($array) {
		$len = count($array);
		for ($i = 0; $i < $len; $i++) $array[$i] = trim($array[$i]);
		return $array;
	}
	
	public static function ReadFile($filePath) {
		$fileContents = file($filePath);
		return FileHelper::CleanArray($fileContents);
	}
	
	public static function ObjectizeFile($filePath) {
		$file = FileHelper::ReadFile($filePath);
		$objectArray = array();
		$len = count($file);
		
		for ($i = 0; $i < $len; $i++) {
			$contents = explode('&', $file[$i]);
			
			//files will have user id first, then other details
			$objectArray[] = new stdClass();
			$objectArray[$i]->id = $contents[0];
			$objectArray[$i]->details = $contents[1];
		}
		return $objectArray;
	}
}
