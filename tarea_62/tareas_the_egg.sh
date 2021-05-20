#!/bin/bash
# rr
echo "Número de tarea para crear plantillas: "
read NEW_TAREA
ORIG_DIR=$(pwd)

[[ -d $NEW_TAREA ]] && echo $NEW_TAREA already exist, aborting && exit

THE_DIR=/mnt/c/users/tutoretza3/the_egg_2021/tareas/tarea_$NEW_TAREA
mkdir $THE_DIR
cd $THE_DIR
pwd

touch Readme_tarea_$NEW_TAREA.txt
echo -e "////////////////////////////////////// \nDescripción de las sub-tareas para la tarea número: \n=============================================\nEstructura de datos\n\nListado de subtareas del ejercicio:\n-----------------------------------\n\n\n//////////////////////////////////////\n\nAdjuntos:\n\n---------------------\nIncidencias: No hay" >> Readme_tarea_$NEW_TAREA.txt
touch Diccionario_t_$NEW_TAREA.txt
#sed -i '1i Aqui va lacabecera'Diccionario_t_$NEW_TAREA.txt
echo -e "Tarea: XX\nId: XX\nTérmino: \nDescripción: \nPhoto:\n///////////// " >> Diccionario_t_$NEW_TAREA.txt
cd $ORIG_DIR
rm -rf $NEW_TAREA
echo "Directorio y plantillas creadas"
