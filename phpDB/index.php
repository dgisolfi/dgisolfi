<?php

define("JSON_KEYS",$_SERVER['DOCUMENT_ROOT'] . '/keys.json');
require_once($_SERVER['DOCUMENT_ROOT'] . '/DatabaseClass.php');

if (!file_exists(JSON_KEYS)) {
	echo("JSON Config File missing!");
	echo "Could not find " + JSON_KEYS;
} else {
	printf("%s %s","Found",JSON_KEYS);
}


$jsonConfig = json_decode(JSON_KEYS);

if (file_exists($jsonConfig) {
	echo $jsonConfig->{'dbHost'};
} else {
	echo "JSON formst error";
}

//Estsablish Database Connectiopn
//$db = Database::getInstance(JSON_KEYS);
// echo "hello";
// $mysqli = $db->getConnection(); 

//Test Connection

// if (!$mysqli) {
//     echo "Error: Unable to connect to MySQL." . PHP_EOL;
//     echo "Debugging errno: " . mysqli_connect_errno() . PHP_EOL;
//     echo "Debugging error: " . mysqli_connect_error() . PHP_EOL;
//     exit;
// }

// echo "Success: A proper connection to MySQL was made! The my_db database is great." . PHP_EOL;
// echo "Host information: " . mysqli_get_host_info($mysqli) . PHP_EOL;

// mysqli_close($mysqli);

// $sql_query = "SELECT foo FROM .....";
// $result = $mysqli->query($sql_query);

?>