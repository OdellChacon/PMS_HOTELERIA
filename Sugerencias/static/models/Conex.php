<?php

	class Conexion{

		static public function Conectar(){
			$link = new PDO("mysql:host=localhost;dbname=colegio" , "root" , "");
			return $link;
		}

	}

?>