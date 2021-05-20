////////////////////////////////////// 
Descripción de las sub-tareas para la tarea número: 62
=============================================
El objetivo de esta tarea es hacer uso de la utilidad de bash, el lenguaje de órdenes para sistemas UNIX. Yo lo había probado anteriormente en una distribución de Linux (ubuntu), pero en esta ocasión he querido hacerlo desde un Sistema Windows 10. Esto es posible porque existe la posibilidad de hacer uso de una consola Linux, y con ella de los comandos bash, de forma nativa en el sistema operativo windows 10. El Subsistema de Windows para Linux (WSL – Windows Subsystem for Linux) es el que se encarga de ello.

Listado de subtareas del ejercicio:
-----------------------------------
Tal como se requiere en la tarea, he escogido tres rutinas que quisera automatizar en mi equipo. Para ello he realizado otros tantos scripts (archivos de código con funciones para automatización de tareas) que son ejecutados desde el terminal para llevar a cabo las acciones necesarias para el cometido de cada rutina.
Rutina 1: 
Rutina 2: Automatizar la creación de carpetas y plantillas de diccionario y README files de las tareas del curso de AI de la escuela The Egg.
Rutina 3: Automatizar la gestión y limpieza de archivos de descarte y archivos inservibles que suelen anegar recurrentemente el escritorio de mi windows 10.

NOTA: Acceso a los archivos de Ubuntu desde Windows 10. Hay que hacerlo desde la terminal de Ubuntu o Powershel a través de wsl
Ver imagen adjunta "explorador de archivos de ubuntu en w10.JPG"

Descripción de los Scripts.
Script 1: Conocer si el usuario actual es el root del equipo. Este script lo he cogido de la web y lo que he tratado de hacer con el es pegarlo en un simple txt y guardarlo, por medio del explorador de archivos que abre wsl (\\wsl$\Ubuntu\home) en el directorio de usuario de ubuntu en mi sistema windows 10. No sin antes darle permisos (chmod a+x root_is_user.sh) al nuevo archivo alojado en el directorio propio de ubuntu en windows, el archivo ha funcionado correctamente.
Script 2: A través de un input en el terminal introducimos un numero. El script se encarga de crear un directorio nombrado convenientemente y de crear las plantillas para esa tarea en archivos de texto simple.
Script 3: Se solicita, por mesio de un input a través del terminal, un nombre al cual se le añadirá la fecha del mes y año actual y creará un directorio en una ruta especificada (.../almacen_de_escritorio). En esa carpeta copiará todos los archivos que encuentre en la carpeta denominada "pseudoescritorio" (carpeta que está en el escritorio y que es la que guarda los archivos de poca importancia). Acto seguido borrará todos los archivos copiados anteriormente.
//////////////////////////////////////

Adjuntos:
Script para a rutina 1: user_is_root.sh
Script para a rutina 2: tareas_the_egg.sh
Script para a rutina 3: desktopclean.sh
Imagen: "explorador de archivos de ubuntu en w10.JPG"
---------------------
Incidencias: 
La activación de esta utilidad que viene de serie en la compilación 14316 de Windows 10, es sencilla en principio, sin embargo al tratar de hacerlo me dió error y tuve que optar por descargar la app Ubuntu que lo hizo sin problema.

///////////////////////
Refs.: 
https://blog.desdelinux.net/shell-bash-y-scripts-todo-sobre-shell-scripting/
https://www.simplified.guide/bash/compile-script