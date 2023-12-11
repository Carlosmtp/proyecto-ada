#Clase Animal
class Animal:
    def __init__(self, animal, grandeza):
        self.nombre_animal = animal
        self.grandeza = grandeza
        self.tipoObjeto = "Animal"

    def getNombreAnimal(self):
        return self.nombre_animal

    def getGrandeza(self):
        return self.grandeza    
    
    def getTipoObjeto(self):
        return self.tipoObjeto

#Clase Escena
class Escena:
    def __init__(self):
        self.animales = ArbolRN()
        self.grandezaEscena = 0
        self.maximo = 0
        self.tipoObjeto = "Escena"

    def agregar_animal(self, animal):
        self.animales.TREE_INSERT(Nodo(animal))
        self.aumentar_grandeza(animal.getGrandeza())

    def aumentar_grandeza(self, cantidad):
        self.grandezaEscena += cantidad

    def printAnimales(self):
        return self.animales.print_tree()
    
    def getAnimales(self):
        return self.animales

    def getGrandeza(self):
        return self.grandezaEscena  
    
    def getMaximo(self):
        return self.animales.TREE_MAXIMUM().getGrandeza()
    
    def getTipoObjeto(self):
        return self.tipoObjeto

#Clase Parte
class Parte:
    def __init__(self):
        self.escenas = ArbolRN()
        self.grandezaParte = 0
        self.totalEscenas = 0
        self.tipoObjeto = "Parte"

    def agregar_escena(self, escena):
        self.escenas.TREE_INSERT(Nodo(escena))
        self.aumentar_grandeza(escena.getGrandeza())
        self.totalEscenas += 1 

    def aumentar_grandeza(self, cantidad):
        self.grandezaParte += cantidad    

    def printEscenas(self):
        return self.escenas.print_tree() 
    
    def getEscenas(self):
        return self.escenas

    def getGrandeza(self):
        return self.grandezaParte     
    
    def getPromedioGrandeza(self):
        return self.grandezaParte/self.totalEscenas
    
    def getTipoObjeto(self):
        return self.tipoObjeto

#Clase Espectaculo    
class Espectaculo:
    def __init__(self):
        self.apertura = None
        self.partes = ArbolRN()
        self.grandezaEspectaculo = 0
        self.totalPartes = 0
        self.tipoObjeto = "Espectaculo"

    def agregar_parte(self, parte):
        self.partes.TREE_INSERT(Nodo(parte))
        self.aumentar_grandeza(parte.getGrandeza())    
        self.totalPartes += 1  

    def aumentar_grandeza(self, cantidad):
        self.grandezaEspectaculo += cantidad

    def printPartes(self):
        return self.partes.print_tree()
    
    def getPartes(self):
        return self.partes

    def getGrandeza(self):
        return self.grandezaEspectaculo   
    
    def getTotalPartes(self):
        return self.totalPartes   

    def getApertura(self):
        return self.apertura    
    
    def setApertura(self, apertura):
        self.apertura = apertura

    def getTipoObjeto(self):
        return self.tipoObjeto    


#Funciones necesarias 
# Complejidad O(n)
def INORDER(nodo, funcion):
    if nodo is not None:
        INORDER(nodo.getHijoIzq(), funcion)
        funcion(nodo.getValor())
        INORDER(nodo.getHijoDer(), funcion)

def imprimir_nombre_animal(nodo):
    print(nodo.getNombreAnimal())

#Imprimir las animales de una escena
def imprimir_escena(escena, funcion=imprimir_nombre_animal):
    print("")
    print("===  Escena  ===")
    INORDER(escena.getAnimales().getRaiz(), funcion)
    print("Grandeza de la escena: ", escena.getGrandeza())

#Imprimir las escenas de una parte
def imprimir_parte(parte, funcion=imprimir_escena):
    print("")
    print("===  Parte  ===")
    print("")
    print("Grandeza total de la parte: ", parte.getGrandeza())
    INORDER(parte.getEscenas().getRaiz(), funcion)

#Imprimir las partes de un espectaculo
def imprimir_espectaculo(espectaculo, funcion=imprimir_parte):
    print("")
    INORDER(espectaculo.getPartes().getRaiz(), funcion)

#Complejidad O(n), ya que debe recorrer todo el diccionario, el diccionario 
# guarda los valores de los animales y su frecuencia en los arboles
#Buscar el mayor o menor valor del diccionario y devuelve una lista con los keys y el valor
def hallarRepeticion(buscarMayor):
    lista = []
    repeticiones = 0
    #Recorre el diccionario
    for key, value in diccionario.items():
        #Si la lista no está vacía y si el valor es mayor al último valor de la lista
        #Si buscarMayor es True, busca el mayor, sino busca el menor
        if lista and ((buscarMayor and value > diccionario[lista[-1]]) or (not buscarMayor and value < diccionario[lista[-1]])):
            #Reemplaza el último key de la lista por el nuevo key
            lista[-1] = key
            #Reemplaza el número de repeticiones por el nuevo valor
            repeticiones = value
        #Si la lista está vacía o si el valor es igual al último valor de la lista    
        elif not lista or value == diccionario[lista[-1]]:
            #Agrega el key a la lista
            lista.append(key)  
            #Actualice el número de repeticiones
            repeticiones = value
    return lista, repeticiones


#Clase Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijo_izq = None
        self.hijo_der = None
        self.padre = None
        self.color = ""

    def getValor(self):
        return self.valor

    def getHijoIzq(self):
        return self.hijo_izq

    def getHijoDer(self):
        return self.hijo_der

    def getPadre(self):
        return self.padre
    
    def getColor(self):
        return self.color  

    def setHijoIzq(self, hijo):
        self.hijo_izq = hijo
        
    def setHijoDer(self, hijo):
        self.hijo_der = hijo

    def setPadre(self, padre):
        self.padre = padre    

    def setColor(self, color):
        self.color = color

#Para guardar la frecuencia de los elementos
diccionario = {}

#Clase Arbol
class ArbolRN:
    def __init__(self):
        self.raiz = None

    def getRaiz(self):
        return self.raiz
    
    # Crea un árbol binario de búsqueda
    # Complejidad: O(nlogn) 
    def TREE_INSERT (self, nodo):
        y = None
        x = self.raiz

        #Si el nodo no es None y si es un animal
        if nodo != None and nodo.getValor().getTipoObjeto() == "Animal":
            #Si el nodo ya existe, aumente su frecuencia
            if nodo.getValor().getNombreAnimal() in diccionario:
                diccionario[nodo.getValor().getNombreAnimal()] += 1
            #Si el nodo no existe, agregue el nodo y su frecuencia
            else:
                diccionario[nodo.getValor().getNombreAnimal()] = 1

        #Mientras x no sea nulo, busca la posición del nodo
        while x != None:
            y = x
            if nodo.getValor().getGrandeza() < x.getValor().getGrandeza() or \
            (nodo.getValor().getGrandeza() == x.getValor().getGrandeza() and nodo.getValor().getMaximo() < x.getValor().getMaximo()):
                x = x.getHijoIzq()
            else:
                x = x.getHijoDer()
        
        #El padre del nuevo nodo será y, recordar que y es una hoja o un arbol vacío
        nodo.setPadre(y)
        #Si el árbol está vacío
        if y == None:
            #El nodo ingresado será la raíz
            self.raiz = nodo
            #El color de la raíz será negro
            nodo.setColor("BLACK")
        #Si el valor del nodo es menor que el valor de y
        elif nodo.getValor().getGrandeza() < y.getValor().getGrandeza() or \
         (nodo.getValor().getGrandeza() == y.getValor().getGrandeza() and nodo.getValor().getMaximo() < y.getValor().getMaximo()):
            y.setHijoIzq(nodo)
            nodo.setColor("RED")
        else:
            y.setHijoDer(nodo)
            nodo.setColor("RED")

        #Garantizar Arbol Rojo y Negro
        if nodo.getPadre() != None and nodo.getPadre().getPadre():
            self.insert_fixup(nodo)

    #Complejidad O(1)
    def LEFT_ROTATE(self, x):
        y = x.getHijoDer()
        x.setHijoDer(y.getHijoIzq())
        if y.getHijoIzq() != None:
            y.getHijoIzq().setPadre(x)
        y.setPadre(x.getPadre())
        if x.getPadre() == None:
            self.raiz = y
        elif x == x.getPadre().getHijoIzq():
            x.getPadre().setHijoIzq(y)
        else:
            x.getPadre().setHijoDer(y)
        y.setHijoIzq(x)
        x.setPadre(y)
            
    #Complejidad O(1)
    def RIGHT_ROTATE(self, y):
        x = y.getHijoIzq()
        y.setHijoIzq(x.getHijoDer())
        if x.getHijoDer() != None:
            x.getHijoDer().setPadre(y)
        x.setPadre(y.getPadre())
        if y.getPadre() == None:
            self.raiz = x
        elif y == y.getPadre().getHijoDer():
            y.getPadre().setHijoDer(x)
        else:
            y.getPadre().setHijoIzq(x)
        x.setHijoDer(y)
        y.setPadre(x)  
            
    #Complejidad O(logn)       
    def insert_fixup(self, nodo):
        #Mientras el padre del nodo no sea nulo y el color del padre sea rojo
        while nodo != self.raiz and nodo.getPadre().getColor() == 'RED':
            #Si el padre del nodo es un hijo izquierdo
            if nodo.getPadre() == nodo.getPadre().getPadre().getHijoIzq():
                #y es el tío del nodo
                y = nodo.getPadre().getPadre().getHijoDer()
                #Si el tío del nodo es rojo    
                if y is not None and y.getColor() == 'RED':
                    #El color del padre del nodo será negro
                    nodo.getPadre().setColor('BLACK')
                    #El color del tío del nodo será negro
                    y.setColor('BLACK')
                    #El color del abuelo del nodo será rojo    
                    nodo.getPadre().getPadre().setColor('RED')
                    #El nodo actual ahora será el abuelo del nodo
                    nodo = nodo.getPadre().getPadre()
                else:
                    #Si el nodo es el hijo derecho de su padre
                    if nodo == nodo.getPadre().getHijoDer():
                        #El nodo actual ahora será el padre del nodo
                        nodo = nodo.getPadre()
                        #Aplique left rotate al nodo actual
                        self.LEFT_ROTATE(nodo)
                    #El color del padre del nodo ahora será negro
                    nodo.getPadre().setColor('BLACK')
                    #El color del abuelo será rojo
                    nodo.getPadre().getPadre().setColor('RED')
                    #Aplique right rotate al abuelo del nodo
                    self.RIGHT_ROTATE(nodo.getPadre().getPadre())
            else:
                y = nodo.getPadre().getPadre().getHijoIzq()
                if y is not None and y.getColor() == 'RED':
                    nodo.getPadre().setColor('BLACK')
                    y.setColor('BLACK')
                    nodo.getPadre().getPadre().setColor('RED')
                    nodo = nodo.getPadre().getPadre()
                else:
                    if nodo == nodo.getPadre().getHijoIzq():
                        nodo = nodo.getPadre()
                        self.RIGHT_ROTATE(nodo)
                    nodo.getPadre().setColor('BLACK')
                    nodo.getPadre().getPadre().setColor('RED')
                    self.LEFT_ROTATE(nodo.getPadre().getPadre())
        #El color de la raiz será negro
        self.raiz.setColor('BLACK')

    #Complejidad O(logn)
    def TREE_MAXIMUM(self):
        x = self.raiz
        while x.getHijoDer() != None:
            x = x.getHijoDer()
        return x.getValor()  
    
    #Complejidad O(logn)
    def TREE_MINIMUN(self):
        x = self.raiz
        while x.getHijoIzq() != None:
            x = x.getHijoIzq()
        return x.getValor()     

from clases import Animal, Escena, Parte, Espectaculo
from time import time

def leer_archivo(filename):
    n=0
    m=0
    k=0
    animales = {} 
    apertura = Parte()
    espectaculo = Espectaculo()
    
    with open(filename, 'r') as file:
        n, m, k = map(int, file.readline().split())
        file.readline()
        #Crear objetos de animales y alamcenarlos en un diccionario
        for i in range(n):
            animal, grandeza = file.readline().strip().split()
            animales[animal] = Animal(animal, int(grandeza))
        file.readline().split()
        # Crear objetos de escenas y objetos de parte
        for i in range((m-1)*k):
            escena = Escena()  # Crea un nuevo objeto Escena en cada iteración
            ani1, ani2, ani3 = map(str, file.readline().split())
            escena.agregar_animal(animales[ani1])
            escena.agregar_animal(animales[ani2])
            escena.agregar_animal(animales[ani3])
            apertura.agregar_escena(escena) 
        espectaculo.setApertura(apertura)    
        file.readline().split()
        for i in range(m-1):
            parte = Parte()
            for j in range(k):
                escena = Escena()  # Crea un nuevo objeto Escena en cada iteración
                ani1, ani2, ani3 = map(str, file.readline().split())
                escena.agregar_animal(animales[ani1])
                escena.agregar_animal(animales[ani2])
                escena.agregar_animal(animales[ani3])
                parte.agregar_escena(escena) 
            espectaculo.agregar_parte(parte)
    return n, m, k, animales, apertura, espectaculo

inicio = time()
n, m, k, animales, apertura, espectaculo = leer_archivo("../test/test2.txt")
fin = time()

print("")
print("Tiempo de ejecución2: ", fin-inicio, " segundos")

def main():
    print("=========== APERTURA ==============")
    imprimir_parte(apertura)
    print("")
    print("=========== M-1 Partes ==============")
    imprimir_espectaculo(espectaculo)

    print("")
    print("=========== DATOS PUNTUALES SOLICITADOS ==============")
    print("")
    lista1, repeticiones1 = hallarRepeticion(False)
    print("Los animales que participaron en menos escenas fueron: ", lista1)
    print("Las escenas en las que participaron fueron: ", repeticiones1)

    print("")
    lista2, repeticiones2 = hallarRepeticion(True)
    print("Los animales que participaron en más escenas fueron: ", lista2)
    print("Las escenas en las que participaron fueron: ", repeticiones2)

    print("")
    print("La escena de menor grandeza total fue: ")
    imprimir_escena(apertura.getEscenas().TREE_MINIMUN())

    print("")
    print("La escena de mayor grandeza total fue: ")
    imprimir_escena(apertura.getEscenas().TREE_MAXIMUM())

    print("")
    print("El promedio de grandeza de todo el espectaculo fue: ")
    print(round(apertura.getPromedioGrandeza(), 2))

inicio = time()
main()
fin = time()

print("")
print("Tiempo de ejecución: ", fin-inicio, " segundos")
