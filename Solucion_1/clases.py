from clase_arbol import ArbolRN, Nodo

#Clase Animal
class Animal:
    def __init__(self, animal, grandeza):
        self.nombre_animal = animal
        self.grandeza = grandeza

    def getNombreAnimal(self):
        return self.nombre_animal

    def getGrandeza(self):
        return self.grandeza    

#Clase Escena
class Escena:
    def __init__(self):
        self.animales = ArbolRN()
        self.grandezaEscena = 0

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

#Clase Parte
class Parte:
    def __init__(self):
        self.escenas = ArbolRN()
        self.grandezaParte = 0

    def agregar_escena(self, escena):
        self.escenas.TREE_INSERT(Nodo(escena))
        self.aumentar_grandeza(escena.getGrandeza())

    def aumentar_grandeza(self, cantidad):
        self.grandezaParte += cantidad    

    def printEscenas(self):
        return self.escenas.print_tree() 
    
    def getEscenas(self):
        return self.escenas

    def getGrandeza(self):
        return self.grandezaParte     

#Clase Espectaculo    
class Espectaculo:
    def __init__(self):
        self.partes = ArbolRN()
        self.grandezaEspectaculo = 0

    def agregar_parte(self, parte):
        self.partes.TREE_INSERT(Nodo(parte))
        self.aumentar_grandeza(parte.getGrandeza())      

    def aumentar_grandeza(self, cantidad):
        self.grandezaEspectaculo += cantidad

    def printPartes(self):
        return self.partes.print_tree()
    
    def getPartes(self):
        return self.partes

    def getGrandeza(self):
        return self.grandezaEspectaculo   

#Complejidad O(n)
def INORDER_ESCENAS(nodo):
    if nodo != None:
        INORDER_ESCENAS(nodo.getHijoIzq())  
        print(nodo.getValor().getNombreAnimal())
        INORDER_ESCENAS(nodo.getHijoDer())       

#Una parte contiene escenas
#Complejidad O(n)
def INORDER_PARTE(nodo):
    if nodo != None:
        INORDER_PARTE(nodo.getHijoIzq())  
        print("")
        INORDER_ESCENAS(nodo.getValor().getAnimales().getRaiz())
        INORDER_PARTE(nodo.getHijoDer())




    


    

















        
