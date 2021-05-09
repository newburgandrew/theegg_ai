# Ejercicio 1 de la Tarea 52
# La definición de algunas funciones y clases están tomadas de Nikhil Kumar Singh (nickzuck_007)
# Las funciones A, B y C son de cosecha propia

###################################################
# Para este ejercicio he decidido (no se si acertadamente, me temo que no :-/ ) usar una linked list.

# definimos dos clases, una para definir un nodo  y otra  para la lista enlzada con sus métodos
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # método para inicializar el head de la lista
    def __init__(self):
        self.head = None

    # método para insertar un elemento nuevo en la lista
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

###################################################################
    # Aqui van los métodos de la clase LinkedList
    # método para eliminar de la lista un número dado, si es que se halla en ella.
    def deleteNode(self, key):
        # Store head node
        temp = self.head
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if (temp == None):
            return Exception
        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

    #########
    # método para imprimir los elementos de la lista
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, " -> ", end='')
            temp = temp.next
        print("")

    #########
    # A: método para sumar los elementos de la lista
    def sumarList(self):
        temp = self.head
        j = 0
        while (temp):
            j = temp.data + j
            print(temp.data, " + ", end='')
            temp = temp.next
        print("Valor de la suma ", j)
        return j

    #########
    #B: Método que devuelve uno a uno los elementos

    def getValor(self, key): #basado en sumarList
        temp = self.head
        j = 0
        while (temp):
            j = temp.data + j
            if temp.data < key:
                #print("ENTRA EN EL CONDICOPNLA", temp.data)
                llist2.push(temp.data)
            temp = temp.next
        return j

    #########
    #C: Método que devuelve uno a uno los elementos
    def getValorATupla(self):
        temp = self.head
        cadena = ""
        while (temp):
            cadena = cadena + str(temp.data) + ", "
            temp = temp.next
            print(cadena)
        return cadena

#####################################################
#####################################################
# Ejercicio 1: Creamos una lista concreta invocando a la clase
x = 1
llist = LinkedList()
while x > 0:
    x = int(input("introduce el número: "))
    if x != 0:
        llist.push(x)
    else:
        print("FIN")

# Ejercicio 1: Invocamos al método de impresión antes definido para obtener la lista impresa en pantalla
print("Created Linked List: ")
llist.printList()


# Ejercicio 2: Invocamos al método de eliminación de un número concreto, a partir de un input prompt
k = int(input("Borrar el numero: "))
if llist.deleteNode(k) is Exception:
    print("No se ha hallado el numero ", k)
else:
    print("Borrado el numero ", k)

print("\nLista resultante tras eliminar el elemento: ")
llist.printList()


# Ejercicio 3: Invocamos al método de suma de todos los elementos de la lista
print("\nSuma resultante de los elementos de la lista: ")
llist.sumarList()


# Ejercicio 4 : Establecemos un número límite y cramos una nueva lista (llist2)  con los valores de la lista que son menores que ese límite establecido.
llist2= LinkedList()
x = input("Introduce un límite para valores para la segunda lista: ")
llist.getValor(int(x))
print("\nLista resultante cón límite: ")
llist2.printList()

# Ejercicio 5: Establecer una tupla con los valores de la "llist" y contar cuantra ocurrencia de cada valor se da en la tupla

res = eval(llist.getValorATupla())  # convertimos la cadena de valores  que nos devuelve la funcion "getValorATupla" en tupla
miTupla = (res) # iniciamos una tupla con los valores recibidos antes
print(miTupla)
print(type(miTupla))
x = int(input("Elige un número para ver cuántas veces se repite: ", ))
print(miTupla.count(x))