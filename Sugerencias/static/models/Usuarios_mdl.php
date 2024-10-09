<?php

require_once "Conex.php";

	class Registro_Mdl{


////////////////////////////////////////////////////////////////Estudiantes//////////////////////////////////////////////////////////////////////////

		static public function Entrada_Datos($tabla,$datos){ //Create 
			$stmt = Conexion::Conectar()->prepare("INSERT INTO $tabla (Nombre, Apellido, Edad, Cedula, Genero, Telefono, Fecha_Nacimiento, Correo, Clave, Direccion, Curso, Condicion, Pais, Estado, Ciudad) VALUES (:Nombre, :Apellido, :Edad, :Cedula, :Genero, :Telefono, :Fecha_Nacimiento, :Correo, :Clave, :Direccion, :Curso, :Condicion, :Pais, :Estado, :Ciudad)");

			$stmt->bindParam(":Nombre",$datos["nombre"], PDO::PARAM_STR);
			$stmt->bindParam(":Apellido",$datos["apellido"], PDO::PARAM_STR);
			$stmt->bindParam(":Edad",$datos["edad"], PDO::PARAM_STR);
			$stmt->bindParam(":Cedula",$datos["cedula"], PDO::PARAM_STR);
			$stmt->bindParam(":Genero",$datos["genero"], PDO::PARAM_STR);
			$stmt->bindParam(":Telefono",$datos["numero"], PDO::PARAM_STR);
			$stmt->bindParam(":Fecha_Nacimiento",$datos["nacimiento"], PDO::PARAM_STR);
			$stmt->bindParam(":Correo",$datos["correo"], PDO::PARAM_STR);
			$stmt->bindParam(":Clave",$datos["clave"], PDO::PARAM_STR);
			$stmt->bindParam(":Direccion",$datos["direccion"], PDO::PARAM_STR);
			$stmt->bindParam(":Curso",$datos["curso"], PDO::PARAM_STR);
			$stmt->bindParam(":Condicion",$datos["condicion"], PDO::PARAM_STR);
			$stmt->bindParam(":Pais",$datos["pais"], PDO::PARAM_STR);
			$stmt->bindParam(":Estado",$datos["estado"], PDO::PARAM_STR);
			$stmt->bindParam(":Ciudad",$datos["ciudad"], PDO::PARAM_STR);

			if ($stmt->execute()) {
				return "ok";
			}else{
				print_r(Conexion::Conectar()->errorInfo());
			}
		}

//////////////////////////////////////////////////////////////////////Padres//////////////////////////////////////////////////////////////////////////

		static public function Envio_Padre_mdl($tabla,$datos){ //Create 
			$stmt = Conexion::Conectar()->prepare("INSERT INTO $tabla(Nombre, Apellido, Edad, Cedula, Nacionalidad, Telefono, Direccion, Ocupacion, Lugar_Trabajo, Telefono_Trabajo) VALUES (:Nombre, :Apellido, :Edad, :Cedula, :Nacionalidad, :Telefono, :Direccion, :Ocupacion, :Lugar_Trabajo, :Telefono_Trabajo)");

			$stmt->bindParam(":Nombre",$datos["Nombre"], PDO::PARAM_STR);
			$stmt->bindParam(":Apellido",$datos["Apellido"], PDO::PARAM_STR);
			$stmt->bindParam(":Edad",$datos["Edad"], PDO::PARAM_STR);
			$stmt->bindParam(":Cedula",$datos["Cedula"], PDO::PARAM_STR);
			$stmt->bindParam(":Nacionalidad",$datos["Nacionalidad"], PDO::PARAM_STR);
			$stmt->bindParam(":Telefono",$datos["Telefono"], PDO::PARAM_STR);
			$stmt->bindParam(":Direccion",$datos["Direccion"], PDO::PARAM_STR);
			$stmt->bindParam(":Ocupacion",$datos["Ocupacion"], PDO::PARAM_STR);
			$stmt->bindParam(":Lugar_Trabajo",$datos["Lugar_Trabajo"], PDO::PARAM_STR);
			$stmt->bindParam(":Telefono_Trabajo",$datos["Telefono_Trabajo"], PDO::PARAM_STR);

			if ($stmt->execute()) {
				return "ok";
			}else{
				print_r(Conexion::Conectar()->errorInfo());
			}
		}

///////////////////////////////////////////////////////////////////Madres/////////////////////////////////////////////////////////////////////////////


		static public function Envio_Madre_mdl($tabla,$datos){ //Create 
			$stmt = Conexion::Conectar()->prepare("INSERT INTO $tabla(Nombre, Apellido, Edad, Cedula, Nacionalidad, Telefono, Direccion, Ocupacion, Lugar_Trabajo, Telefono_Trabajo) VALUES (:Nombre, :Apellido, :Edad, :Cedula, :Nacionalidad, :Telefono, :Direccion, :Ocupacion, :Lugar_Trabajo, :Telefono_Trabajo)");

			$stmt->bindParam(":Nombre",$datos["Nombre"], PDO::PARAM_STR);
			$stmt->bindParam(":Apellido",$datos["Apellido"], PDO::PARAM_STR);
			$stmt->bindParam(":Edad",$datos["Edad"], PDO::PARAM_STR);
			$stmt->bindParam(":Cedula",$datos["Cedula"], PDO::PARAM_STR);
			$stmt->bindParam(":Nacionalidad",$datos["Nacionalidad"], PDO::PARAM_STR);
			$stmt->bindParam(":Telefono",$datos["Telefono"], PDO::PARAM_STR);
			$stmt->bindParam(":Direccion",$datos["Direccion"], PDO::PARAM_STR);
			$stmt->bindParam(":Ocupacion",$datos["Ocupacion"], PDO::PARAM_STR);
			$stmt->bindParam(":Lugar_Trabajo",$datos["Lugar_Trabajo"], PDO::PARAM_STR);
			$stmt->bindParam(":Telefono_Trabajo",$datos["Telefono_Trabajo"], PDO::PARAM_STR);

			if ($stmt->execute()) {
				return "ok";
			}else{
				print_r(Conexion::Conectar()->errorInfo());
			}
		}


//////////////////////////////////////////////////////////////Representantes//////////////////////////////////////////////////////////////////////////


		static public function Envio_Representante_mdl($tabla,$datos){ //Create 
			$stmt = Conexion::Conectar()->prepare("INSERT INTO $tabla(Nombre, Apellido, Edad, Cedula, Parentesco, Nacionalidad, Telefono, Direccion, Ocupacion, Lugar_Trabajo, Telefono_Trabajo, Telefono_Emergencia) VALUES (:Nombre, :Apellido, :Edad, :Cedula, :Parentesco, :Nacionalidad, :Telefono, :Direccion, :Ocupacion, :Lugar_Trabajo, :Telefono_Trabajo, :Telefono_Emergencia)");

			$stmt->bindParam(":Nombre",$datos["Nombre"], PDO::PARAM_STR);
			$stmt->bindParam(":Apellido",$datos["Apellido"], PDO::PARAM_STR);
			$stmt->bindParam(":Edad",$datos["Edad"], PDO::PARAM_STR);
			$stmt->bindParam(":Cedula",$datos["Cedula"], PDO::PARAM_STR);
			$stmt->bindParam(":Parentesco",$datos["Parentesco"], PDO::PARAM_STR);
			$stmt->bindParam(":Nacionalidad",$datos["Nacionalidad"], PDO::PARAM_STR);
			$stmt->bindParam(":Telefono",$datos["Telefono"], PDO::PARAM_STR);
			$stmt->bindParam(":Direccion",$datos["Direccion"], PDO::PARAM_STR);
			$stmt->bindParam(":Ocupacion",$datos["Ocupacion"], PDO::PARAM_STR);
			$stmt->bindParam(":Lugar_Trabajo",$datos["Lug_Trabajo"], PDO::PARAM_STR);
			$stmt->bindParam(":Telefono_Trabajo",$datos["Telefono_Trabajo"], PDO::PARAM_STR);
			$stmt->bindParam(":Telefono_Emergencia",$datos["Numero_Emergencia"], PDO::PARAM_STR);

			if ($stmt->execute()) {
				return "ok";
			}else{
				print_r(Conexion::Conectar()->errorInfo());
			}
		}

	}

?>