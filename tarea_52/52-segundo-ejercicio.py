# Ejercicio 2 de la Tarea 52

###################################################
# dos variables auxiliares para el promt de entrada de datos
mensajeGrado = "PRIM: "
mensajedeEntradaDatos = "Introduce un nombre para el curso de "

# Función de carga de nombres común a las dos listas
def cargarNombres(alumnos):
    nombre = input(mensajedeEntradaDatos + mensajeGrado)
    while nombre != "x":
        alumnos.add(nombre)
        nombre = input(mensajedeEntradaDatos + mensajeGrado)
    return alumnos

###################################################
# Inicializamos una conjunto (primaria) y seguido le pasamos la función de carga
grupoPrimaria = set()
grupoPrimaria = cargarNombres(grupoPrimaria)

# Cambiamos una parte del mensaje del prompt y seguido inicializamos una conjunto (Secundaria) y seguido le pasamos la función de carga
mensajeGrado = "SEC: "
grupoSecundaria = set()
grupoSecundaria = cargarNombres(grupoSecundaria)

###################################################
# Finalmente ejecutamos las distintas operaciones solicitadas en la tarea 52:

print("Alumnos del grupo de primaria: ")
for nombre in grupoPrimaria:
    print(nombre)

print("Alumnos del grupo de secundaria: ")
for nombre in grupoSecundaria:
    print(nombre)

# Ejercicio 1: Listar, sin repeticón, todos los nombres de  ambos grupos
print("MODO A: Todos los alumnos, de los dos grupos:")
for nombre in grupoPrimaria | grupoSecundaria:
    print(nombre)

# Ejercicio 2: Informar qué nombres se repiten entre los alumnos de nivel primario y secundario
print("Nombres que se repiten en los dos grupos:")
for nombre in grupoPrimaria.intersection(grupoSecundaria):
        print(nombre)

# Ejercicio 3: Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
print("Nombres de primaria que no están en secundaria:")
for nombre in grupoPrimaria.difference(grupoSecundaria):
    print(nombre)

