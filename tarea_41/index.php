<?php
echo "TEXTO A ANALIZAR:";
// El código aquí presentado puede ejecutarse accediendo al servidor en el que se aloja: http://www.berezhaziku.eus/autodiagnostico/index.php
echo "<br>";
echo "<br>";
echo "En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento?Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo, ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que se encarga de pensar, y hasta cantamos juntos la canción de Annie.Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así.";
echo "<br>";
echo "------------------------------------------------------";
$string2 = "En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento? Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo, ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno. Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que se encarga de pensar, y hasta cantamos juntos la canción de Annie. Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así.";

//Primeramente con la función _preg_replace_ realiza una búsqueda de las comas o de las o de todos aquellso s caractereos que no sean letras o numeros, ignorando las distinción de mayúscula o minúscula (/i) y realiza una sustitución por un carater vacío ('').
$string = preg_replace('/[,]|[^a-z,ó,á,é,í,ú,ñ,0,1-9]+/i', ' ', $string2);

// Seguidamente
preg_match_all('/(\S{1,})|(^,)/', $string, $miarray);

//En este punto convierto el array multidimensional que convierte la funcion anterioy en un array de una dimensión
$arraySingle = call_user_func_array('array_merge', $miarray);
//Cuennto las entradas del array de terminos únicos y lo divido entre 3; la razón es que nos se aun porqué, la funcion preg_match_all genera por triplicado los términos del texto.
$countValues = count($arraySingle)/3;
$countcharacters = count($tring);
echo "------------------------------------------------------";
echo "<br>";
echo "Número de palabras totales: ";
print_r($countValues);
echo "<br>";
echo "Número de caracteres totales: ";
echo preg_match_all("/[\S]/", $string, $matches); 
echo "<br>";
echo "Las 3 palabras más repetidas en el texto: ";
echo "<br>";

$values = array_count_values($arraySingle);
arsort($values);
$top = array_slice($values, 1, 3); // get top 3
print_r($top);
echo "<br>";
echo "<br>";
echo "Listado de las palabras individuales: ";
echo "<br>";
echo "<br>";
for ($i = 0; $i < $countValues; $i++) {
echo $arraySingle[$i];
echo "<br>";
}
echo "<br>";
?>


