# Código prestado y arreglado  https://www.geeksforgeeks.org/
# Método de búsqueda "Secuencial"
# Danda una lista, le preguntamos por un número concreto y que no diga si está en la lista o no y,
# en caso afirmativo, que nos diga su posición

def busqueda_secuencial(arr2, n):
    i = 0
    largo = len(arr2)
    while i < len(arr2) & largo != 0:
        if arr2[i] == n:
            print("Hallado - Iteración num.: ", i)
            print("El número solicitado se encuentra en la posición: ", i)
            i = i + 1
            #return 1
        else:
            print("NO Hallado - Iteración num.: ", i)
            i = i + 1
            #return -1

# Se crea una lista  en la cual realizar la búsqueda binaria
arr = [3, 56, 21, 24, 33, 874, 123, 66, 1000, 23, 45, 65, 56]

## Aqui creo una copia de l alisat origibnal pero ya ordenada
arr2 = sorted(arr, reverse=False)

## A continuación se propone un número a buscar en la lista
n = 3

# llamo a la función de búsqueda con los dos parámetros: la lista y el número a buscar...
result = busqueda_secuencial(arr2, n)
