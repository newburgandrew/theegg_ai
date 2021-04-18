#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 19:26:45 2021

@author: andrew newburg
""" 
import random
import time 


print("Batalla de Pokemons")

class luchadorPokemon:
	# Creamos una clase de luchador para instanciarla despues en dos luchadores, o más si hicieran falta
	species = "clase de luchador"

def __init__(self, nombre, vida, fuerza, turno):
    self.nombre = nombre
    self.vida = vida
    self.fuerza = fuerza
    self.turno = turno

########### PARTE 1 #######################################
# Vamos a crear los dos luchadores a partir de la clase definida antes   	 
Pikachu = luchadorPokemon()
Pikachu.nombre= "Pikachu"
Pikachu.vida = 100
Pikachu.fuerza= 46
Pikachu.turno = 1

JiggyPuff = luchadorPokemon()
JiggyPuff.nombre= "JiggyPuff"
JiggyPuff.vida = 100
JiggyPuff.fuerza= 48
JiggyPuff.turno = 0
########################################

########### PARTE 2: EVENTO LUCHA #######################################
# comprobamos que estan los dos con vida, comprobación cíclica que mantiene la lucha y que cesará en cuanto muera uno
# de los luchadores, es decir, en cuanto se quede en vida 0 o menor

while (Pikachu.vida > 0 and JiggyPuff.vida > 0):

    
    ########### PARTE 2-A #######################################
    # Vamos a crear un ataque modificado por una variable random que atenua la fuerza de ataque de cada uno de los dos luchadores. 
    # Lo hacemos así para que la fuerza de ataque de cada uno pueda variar ligeramente y poder así da oportunidad de triunfo
    # al luchador que cuenta con una menor fuerza de ataque propia. Igualmente podríamos haber metido esta variación random en la fuerza inicial establecida
    # en la instancia de la clase (de cada personje) pero he preferido hacerlo como sigue porque permitiría hacer más ajustes de fuerza. por ejemplo que en 
    # función del daño recibido, su ataque se atenue más o menos o incluso se aumente en el próximo turno.

    x = Pikachu.fuerza
    y = JiggyPuff.fuerza

    fuerza1modif = (random.randint(10, 100))
    ataque1 = x*fuerza1modif/100

    fuerza2modif = (random.randint(10, 100))
    ataque2 = y*fuerza2modif/100


    ########### PARTE 2-B #######################################
    # comprobamos quién tiene turno y realiza el ataque, uno a uno alternativamente
    if Pikachu.turno == 1: 
        print("lucha Pikachu con fuerza ", ataque1)
        JiggyPuff.vida = JiggyPuff.vida - ataque1;
        # intercambio de turno para que en el siguiente ciclo ataque el contrario.
        Pikachu.turno = 0
        JiggyPuff.turno = 1
        print("lucha en curso.....................");
    else: 
        print("lucha JiggyPuff con fuerza ", ataque2)
        Pikachu.vida = Pikachu.vida - ataque2;
        # intercambio de turno para que en el siguiente ciclo ataque el contrario
        JiggyPuff.turno = 0
        Pikachu.turno = 1
        print("lucha en curso.....................");
    
    
########### PARTE 3: RESULTADO DE LA LUCHA #######################################  

# Sacamos or pantalla el nivel de vida de cada uno y en función de ello, el ganador

print("Vida de Pikachu:", int(Pikachu.vida), "--- Vida de JiggyPuff:", int(JiggyPuff.vida))
if Pikachu.vida > JiggyPuff.vida:
    print("GANA Pikachu")
else:
    print("GANA JiggyPuff")
print("fin de la lucha de pokemons")

        
