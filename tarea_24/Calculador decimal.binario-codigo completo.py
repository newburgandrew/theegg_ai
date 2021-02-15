#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 00:33:37 2021

@author: alberto-mac
"""
x=1
while x >= 0:
    try:
        print("Convertidor de número de base decimal a binario. Para salir del programa basta con introducir cualquier número negativo."); x = int(input("Introduce un número decimal: "))
        listbin = []
        if x <= 0:
            raise ValueError("Introducir sólamente números decimales positivos!")
        while (x/2 != 0):
            listbin.append(x%2)
            x = x//2 
    
        concatenador = lambda listbin: int(''.join(str(i) for i in reversed(listbin)))
        print("Lista: ", listbin, " Resultado:", str(concatenador(listbin)) +'\n' +'\n' +'*****************************************')
    except ValueError as ve:
        print(ve)
