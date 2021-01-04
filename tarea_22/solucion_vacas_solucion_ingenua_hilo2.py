#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 14:59:11 2021

@author: alberto-mac_linux
"""

x = 0
candidato = "V"
pma = 700
prod_leche_total = 0
print("INICIO DEL SCRIPT - HILO 2 ///////////////////////////////////////////////////////////")
print("/////////////////////////////////////////////////////////////////////////////////////")
print("/////////////////////////////////////////////////////////////////////////////////////")
## Creamos un array con las 6 vacas, su nombre, peso y producción y dejamos dos  elementos inicializados a 0 que serán los que contrendrán los índices calculados porsteiormente
vacas = [['v1', 360, 40, 0, 0, 0], ['v2', 250, 35, 0, 0, 0], ['v3', 400, 43, 0, 0, 0], ['v4', 180, 28, 0, 0, 0], ['v5', 50, 12, 0, 0, 0], ['v6', 90, 13, 0, 0, 0]]
## Calculamos los  tres indices: el de produccion , el de carga y el indice global que los combian a ambos
for i in range(len(vacas)):
	i_de_prod = float(round(vacas[i][2] / vacas[i][1], 3)) 
	print("Ind Prod: ", i_de_prod)
	vacas[i][3] = i_de_prod 

for j in range(len(vacas)):
	i_de_carg = float(round(vacas[j][1] / pma, 3)) 
	print("Ind PMA: ", i_de_carg)
	vacas[j][4] = i_de_carg 
    
for k in range(len(vacas)):
	i_glo = float(round(vacas[k][3] + vacas[k][4], 3)) 
	print("Ind Glob: ", i_glo)
	vacas[k][5] = i_glo 
    
print(vacas)

    
##algotiymo de ordenamiento, tipo lambda
print("///////////////////////////////////////////////////////////")
print("///////////////////////////////////////////////////////////")
print("///////////////////////////////////////////////////////////")
print("Ordenamos el array en función del ÍNDICE GLOBAL: ")
lista_elegidas = []
def fifthItem(ls):
    #return the fifth item of the list
    return ls[5]
    
i = 0  
vacas.sort(key=fifthItem, reverse=True); #print(vacas)
while x <= 700:
	x = x + int(vacas[i][1]); #print(x, "Vaca candidata para cargar al camión: ", str(vacas[i][0]))
    #Como este hilo 2 es la continuacion del caso planteado en el hilo 1, lo unico qu ehacemos es seleccioanr directamente la vaca 1
	if (x < 700) and (vacas[i][0] == 'v1'):
			print("Vaca seleccionada para cargar al camión: ", vacas[i][0], " y su peso: ", vacas[i][1]); lista_elegidas.append(vacas[i][0]); prod_leche_total = prod_leche_total + vacas[i][2]
			x = x + int(vacas[i][1]); i += 1; print(lista_elegidas)
	else:
			print("Descartado el", vacas[i][0], "por no ser la vaca 1", vacas[i][1]); i += 1
			x = x - int(vacas[i-1][1]); #print(x)
			print("Peso acumulado al camión: ", x); y = x
x = x - int(vacas[i-1][1]); print(x)
y=x
print("Peso acumulado al camión en esta ronda: ", x)

print("HILO 2 - ///////////////////////////////////////////////////////////")
print("Peso acumulado del paso anterior: ", y)
print("Ordenamos el array en función del ÍNDICE DE PRODUCCIÓN: ")
def thirdItem(ls):
    #return the fourth item of the list
    return ls[3]

i = 0  


#print(x, "eta", y, "eta", i)
vacas.sort(key=thirdItem, reverse=True); #print(vacas)
while y <= 700:
	if y <= 700:
			y = y + int(vacas[i][1]); #print(x, "eta ahora", y, "eta", i)
			#print("x is menos than 700")
			print("candidato:", vacas[i][0], " y su peso ", vacas[i][1]); lista_elegidas.append(vacas[i][0]); prod_leche_total = prod_leche_total + vacas[i][2]
			#print("Peso acumulado al camión: ", y)
			i += 1
	elif y >= 700:
			print("Descartado el", vacas[i][0], " por exceso de peso: ", vacas[i][1]);
			print("Peso acumulado final: ", y)
			exit(0)
if y > 700:
        print("El último animal excedería el peso hasta ", y , " kg. por lo que se descuenta del cargamento")
        y = y - int(vacas[i-1][1]); lista_elegidas.remove(vacas[i-1][0]); prod_leche_total = prod_leche_total - vacas[i-1][2]
print("///////////////////////////////////////////////////////////")
print("SOLUCIÓN. ////////////////////////////////////////////////")
print("Vacas escogidas: ", lista_elegidas)
print("Producción de leche: ", prod_leche_total)
print("Peso acumulado FINAL en el camión: ", y)
print("///////////////////////////////////////////////////////////")
print("///////////////////////////////////////////////////////////")