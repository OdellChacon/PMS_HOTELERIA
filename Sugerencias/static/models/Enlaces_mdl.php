<?php

    class Enlaces_Mdl{

        static public function Redirecciones($Enlaces){
            if($Enlaces == "listadmin" || $Enlaces == "lista_estudiantes" || $Enlaces == "Lista_Docentes" 
            || $Enlaces == "Registro_Estudiante" || $Enlaces == "Admin_Reg" || $Enlaces == "Doc_Reg" 
            || $Enlaces == "Carga_Notas" || $Enlaces == "editar" ||$Enlaces == "editar_adm" ||$Enlaces == "editar_doc" 
            || $Enlaces == "Calificar" || $Enlaces == "generar_materias" || $Enlaces == "pag_pri" || $Enlaces == "asignar_grupos" 
            || $Enlaces == "asignatura" || $Enlaces == "registro_padres" || $Enlaces == "registro_madres" || $Enlaces == "registro_representantes" 
            || $Enlaces == "horarios" || $Enlaces == "lista_horarios" || $Enlaces == "rep_horario" || $Enlaces == "asignar_grupos" 
            || $Enlaces == "listados_menu" || $Enlaces == "lista_salones" || $Enlaces == "ejemplo" || $Enlaces == "carta_conducta" || $Enlaces == "imprimir"){
                $modulo = "views/modules/".$Enlaces.".php";
            }

            elseif ($Enlaces == "index"){
                $modulo = "views/modules/Menu_Principal.php";
            }

            else{
                $modulo = "views/modules/error_404.php";
            }

            return $modulo;
        }


    }

?>