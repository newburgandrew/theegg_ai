# Código prestado y arreglado  https://www.geeksforgeeks.org/
# Método de búsqueda "Binario"
# Danda una lista, le preguntamos por un número concreto y que no diga si está en la lista o no y,
# en caso afirmativo, que nos diga su posición

def busqueda_binaria(arr, n):
    izq = 0
    der = len(arr) - 1
    medio = 0
    i = 1

    while izq <= der:

        medio = (der + izq) // 2

        # En caso de que x sea mayor que el término medio de la lista, pasamos de la parte izquierda...
        if arr[medio] < n:
            izq = medio + 1

        # En caso de que x sea mayor que el término medio de la lista, pasamos de la parte derecha ...
        elif arr[medio] > n:
            der = medio - 1

        # En este tercer caso sería que x es justo el término medio.
        else:
            return medio
        print("Número de iteraciones: ", i)
        i = i + 1
    # Si llegamos aquí, es que el numero a buscar no se halla en la lista
    return -1

# Se crea una lista  en la cual realizar la búsqueda binaria
arr = [3, 56, 21, 24, 33, 874, 123, 66, 1000, 23, 45, 65, 56]

## Aqui creo una copia de l alisat origibnal pero ya ordenada
arr2 = sorted(arr, reverse=False)

## Aqui solo muestro por consola los valores de la lista ya ordenados
for i in range(len(arr)):
    print ("Posición ", i, " ----> item:", arr2[i])

## A continuación se propone un número a buscar en la lista
n = 10088

# llamo a la función de búsqueda con los dos parámetros: la lista y el número a buscar...
result = busqueda_binaria(arr2, n)

if result != -1:
    print("El número solicitado se encuentra en la posición: ", str(result))
else:
    print("El número solicitado NO se encuentra en la lista")