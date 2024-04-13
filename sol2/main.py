from time import time
import argparse

#Clase Nodo
class Nodo:
    def __init__(self, data, grandeza):
        self.data = data 
        self.next = None #almacenará el nodo siguiente
        self.grandeza = grandeza #almacenará la grandeza de la tupla 

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def getGrandeza(self):
        return self.grandeza

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next   

    def setGrandeza(self, grandeza):
        self.grandeza = grandeza         

#Clase Lista Enlazada
class LinkedList:
    def __init__(self):
        self.head = None #almacenará el primer nodo de la lista

    def getHead(self):
        return self.head   

    def setHead(self, nodo):
        self.head = nodo   

    def insert(self, data, grandeza):
        #El elemento a insertar será un nodo
        new_node = Nodo(data, grandeza)
        #Si la lista está vacía, el nuevo nodo será el primero
        if not self.head:
            self.head = new_node
        #sino,   
        else:
            #se crea un nodo temporal que inicial mente será 
            #el primer elemento de la lista
            temp = self.head
            #se recorre la lista hasta el último nodo y 
            #se agrega el nuevo nodo.  
            while temp.next:
                #Esto hace que vaya pasando los nodos
                temp = temp.next
            #Cuando el último nodo tenga en next un None, significa que es el último, y se añade el nuevo valor en el next del nodo.    
            temp.next = new_node

# Complejidad O(n), donde n es el número de líneas en el archivo.
#Lee un archivo y crea pilas que contiene pilas o tuplas.
def leer_archivo(filename):
    n = 0
    m = 0
    k = 0

    #Será un diccionario
    animales = {}
    #Será una lista enlazada de tuplas
    apertura = LinkedList()
    #Será una lista enlazada que contiene pilas de partes 
    #y estas partes contienen tuplas
    partes = LinkedList()

    #Se abre el archivo
    with open(filename, 'r') as file:
        n, m, k = map(int, file.readline().split())
        file.readline()
        #Crear tuplas de animales y almacenarlos en un diccionario
        for i in range(n):
            animal, grandeza = file.readline().strip().split()
            animales[animal] = int(grandeza)

        file.readline().split()
        for i in range((m - 1) * k):
            ListaEnt = LinkedList()
            #La apertura tendrá tuplas de escenas
            ani1, ani2, ani3 = file.readline().strip().split()
            ListaEnt.insert(ani1, animales[ani1])
            ListaEnt.insert(ani2, animales[ani2])
            ListaEnt.insert(ani3, animales[ani3])
            gran = animales[ani1] + animales[ani2] + animales[ani3]
            apertura.insert(ListaEnt, gran)
        file.readline().split()
        for i in range(m - 1):
            parte = LinkedList()
            granTotal = 0
            for j in range(k):
                ListaEnt = LinkedList()
                #La apertura tendrá tuplas de escenas
                ani1, ani2, ani3 = file.readline().strip().split()
                ListaEnt.insert(ani1, animales[ani1])
                ListaEnt.insert(ani2, animales[ani2])
                ListaEnt.insert(ani3, animales[ani3])
                gran = animales[ani1] + animales[ani2] + animales[ani3]
                parte.insert(ListaEnt, gran)
                granTotal += gran
            #Inserta cada parte (lista enlazada) que contiene tuplas en partes(lista enlazada) que contiene)    
            partes.insert(parte, granTotal)
    return n, m, k, animales, apertura, partes

#Imprimir todos los elementos de una lista enlazada, 
#incluyendo las listas enlazadas anidadas
#Complejidad: O(n)
def recorrerLista(head, mensaje):
    current = head
    while current is not None:
        # Si el dato actual es otra lista enlazada, recórrela recursivamente
        if isinstance(current.data, LinkedList):
            print(mensaje)
            recorrerLista(current.data.getHead(), mensaje)
            print("Grandeza: ", current.getGrandeza())
        else:
            # Procesa el dato actual
            print(current.getData())
        current = current.getNext()

#Complejidad: O(n)
#Cuenta cunatas veces se repite un animal en las escenas        
def contarRepetidos(linked_list):
    current = linked_list.getHead()
    dict_repetidos = {}
    while current is not None:
        # Si el dato actual es otra lista enlazada, recórrela recursivamente
        if isinstance(current.data, LinkedList):
            dict_repetidos_anidados = contarRepetidos(current.data)
            for key, value in dict_repetidos_anidados.items():
                if key in dict_repetidos:
                    dict_repetidos[key] += value
                else:
                    dict_repetidos[key] = value
        else:
            # Procesa el dato actual
            if current.getData() in dict_repetidos:
                dict_repetidos[current.getData()] += 2
            else:
                dict_repetidos[current.getData()] = 2
        current = current.getNext()    
    return dict_repetidos

#Complejidad: O(n + m)
def hallarRepetidos (apertura, bool):
    diccionario = contarRepetidos(apertura)
    repeticion = 0
    lista = []

    for key, value in diccionario.items():
        if not lista or (value > repeticion and bool) or (value < repeticion and not bool):
            lista = [key]
            repeticion = value
        elif value == repeticion:
            lista.append(key)
            repeticion = value

    return lista, repeticion            

#Complejidad O(n)
def get_max_value(input):
    if isinstance(input, Nodo):
        if isinstance(input.getData(), LinkedList):
            current = input.getData()

            max_value = current.getHead().getGrandeza()
            current = current.getHead().getNext()
            while current is not None:
                if current.getGrandeza() > max_value:
                    max_value = current.getGrandeza()
                current = current.getNext()
            return max_value

# Complejiad O(n)
# Función para dividir la lista en mitades
def split_list(head):
    if not head or not head.getNext():
        return head, None

    slow = head
    fast = head.getNext()

    while fast:
        fast = fast.getNext()
        if fast:
            fast = fast.getNext()
            slow = slow.getNext()

    mid = slow.getNext()
    slow.setNext(None)
    return head, mid

# Complejidad O(n+m)
# Función para combinar dos listas ordenadas
def merge(left, right):
    dummy_node = Nodo(0, 0)
    current = dummy_node

    while left and right:
        if left.getGrandeza() < right.getGrandeza() or (left.getGrandeza() == right.getGrandeza() and get_max_value(left) < get_max_value(right)):
            current.setNext(left)
            left = left.getNext()
        else:
            current.next = right
            right = right.getNext()
        current = current.getNext()

    current.next = left if left else right
    return dummy_node.getNext()

# Complejidad O(n log n)
# Función principal de Merge Sort para la lista enlazada
def merge_sort(head):
    if not head or not head.getNext():
        return head

    left, right = split_list(head)
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

# Complejidad O(n log n)
def merge_sort_parte(apertura):
    apertura.setHead(merge_sort(apertura.getHead()))

# Complejidad O(n log n)
def merge_sort_escena_parte(partes):
    merge_sort_parte(partes)
    current = partes.getHead()
    while current is not None:
        current.getData().setHead(merge_sort(current.getData().getHead()))
        current = current.getNext()   
    current2 = partes.getHead()   
    while current2 is not None:
        merge_sort_animales_parte(current2.getData())
        current2 = current2.getNext()

# Complejidad O(n log n)
def merge_sort_animales_parte(partes):
    current = partes.getHead()
    while current is not None:
        current.getData().setHead(merge_sort(current.getData().getHead()))
        current = current.getNext()        

# Complejidad O(1)    
def menorEscena(apertura):
    return apertura.getHead().getData(), apertura.getHead().getGrandeza()

# Complejidad O(n)
def mayorEscena(apertura):
    current = apertura.getHead()

    while current.getNext() is not None:
        current = current.getNext()

    return current.getData(), current.getGrandeza()

# Complejidad O(n)
def promedioGrandeza(linked_list):
    current = linked_list.getHead()
    suma = current.getGrandeza()
    contador = 1
    current = current.getNext()
    while current is not None:
        suma += current.getGrandeza()
        contador += 1
        current = current.getNext()
    return suma / contador
        
def main (filename):

    time1 = time()
    n, m, k, animales, apertura, partes = leer_archivo(filename)

    print(" ==== Apertura ==== \n")
    merge_sort_parte(apertura)
    merge_sort_animales_parte(apertura)
    recorrerLista(apertura.getHead(), "==== Escena ====\n")
    print("")
    print(" ==== (M-1) partes ==== \n")
    merge_sort_escena_parte(partes)
    recorrerLista(partes.getHead(), "")
    print("")
    print("Animales que participaron en menos escenas: ")
    lista, repeticion = hallarRepetidos(apertura, False)
    print(lista)
    print("Repeticiones: ", repeticion)
    print("")
    print("Animales que participaron en más escenas: ")
    lista, repeticion = hallarRepetidos(apertura, True)
    print(lista)
    print("Repeticiones: ", repeticion)
    print("")
    print("La escena con menor grandeza fue: ")
    escena, grandeza = menorEscena(apertura)
    recorrerLista(escena.getHead(), "\n")
    print("Grandeza de la escena:", grandeza)
    print("")
    print("La escena con mayor grandeza fue: ")
    escena, grandeza = mayorEscena(apertura)
    recorrerLista(escena.getHead(), "\n")
    print("Grandeza de la escena:", grandeza)
    print("")
    print("Promedio de la grandeza total del espectáculo: ", round(promedioGrandeza(apertura),2))
    time2 = time()

    print("Tiempo de ejecución: ", time2 - time1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Nombre del archivo de entrada")
    args = parser.parse_args()
    main(args.filename)


