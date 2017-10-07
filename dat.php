<?php
  try
{

$db = new PDO('sqlite:users.db');


$doctor = $_POST["doctor"];
$intake = $_POST["intake"];
$medicine = $_POST["medicine"];
$message = $_POST["message"];


//Insert record  

$db->exec("INSERT INTO registered_users (doctor, intake, medicine, message) VALUES ('$doctor', '$intake', '$medicine', '$message');");

}
catch(PDOException $e)
{
print 'Exception : ' .$e->getMessage();
}

?>
