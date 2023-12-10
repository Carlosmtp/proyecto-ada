from clase_arbol import ArbolRN, Nodo, diccionario

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

#Complejidad O(n)
def hallarRepeticion(buscarMayor):
    lista = []
    repeticiones = 0
    for key, value in diccionario.items():
        if lista and ((buscarMayor and value > diccionario[lista[-1]]) or (not buscarMayor and value < diccionario[lista[-1]])):
            lista[-1] = key
            repeticiones = value
        elif not lista or value == diccionario[lista[-1]]:
            lista.append(key)  
            repeticiones = value
    return lista, repeticiones



           




    


    

















        
