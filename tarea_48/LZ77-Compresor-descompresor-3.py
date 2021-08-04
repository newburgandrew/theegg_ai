# -*- coding: utf-8 -*-
# codigo obtenido de https://www.programmersought.com y ajustado a la tarea por a. uribarri
import sys
"""
Spyder Editor

This is a temporary script file.
"""

largo = 0 #matched length
ventana = 10 #maxima aparetura de ventana.
posicion = 0 #esta variable marca la posición en la que estamos obteniendo

cadenatexto = "abracadabrayabracadadddsdsdsso"
print("COMIENZO //////////////////////////////////////")
print("La cadena original sin comprimir ocupa:", sys.getsizeof(cadenatexto), "bytes")

cadenatexto_comprimida = list() #la lista en la que comporndremos los 3 datos
while True:
    if posicion - ventana < 0:
        match = cadenatexto[0:posicion]
        #print(match)
    else:
        match = cadenatexto[posicion - ventana:posicion]

    while match.find(cadenatexto[posicion:posicion + largo + 1]) != -1:
        largo += 1

    first = match.find(cadenatexto[posicion:posicion + largo])
    if posicion - ventana > 0:
        first += posicion - ventana
    if largo != 0: #si el promer elemnto de 
        a = (posicion - first, largo, cadenatexto[posicion + largo])
        cadenatexto_comprimida.append(a)
        posicion += largo + 1

    else:
        b = (0,0,cadenatexto[posicion])
        cadenatexto_comprimida.append(b)
        posicion +=1

    largo = 0
    if posicion == len(cadenatexto):
        break
print("COMPRESION //////////////////////////////////////")
print(cadenatexto_comprimida)
print("La cadena comprimida ocupa:", sys.getsizeof(cadenatexto_comprimida), "bytes")

print("DESCOMPRESION //////////////////////////////////////")
descomprimida = ""
for s in cadenatexto_comprimida:
    if s[0] != 0:
        descomprimida += descomprimida[(len(descomprimida) - s[0]): (len(descomprimida) - s[0] + s[1])]
    descomprimida += s[2]
print("La cadena ya descomprimida ocupa:", sys.getsizeof(descomprimida), "bytes")
print(descomprimida)