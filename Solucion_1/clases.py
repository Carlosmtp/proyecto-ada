# Clase Animal
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
        self.animales = ArbolBinarioBusqueda()
        self.grandezaEscena = 0

    def agregar_animal(self, nodo_animal):
        self.animales.TREE_INSERT(nodo_animal)
        self.aumentar_grandeza(nodo_animal.getValor().getGrandeza())

    def aumentar_grandeza(self, cantidad):
        self.grandezaEscena += cantidad

    def getAnimales(self):
        return self.animales.print_tree()

    def getGrandeza(self):
        return self.grandezaEscena    

#Clase Parte
class Parte:
    def __init__(self):
        self.escenas = []
        self.grandezaParte = 0

    def agregar_escena(self, escena):
        self.escenas.append(escena)
        self.aumentar_grandeza(escena.grandezaEscena)

    def aumentar_grandeza(self, cantidad):
        self.grandezaParte += cantidad    

    def getEscenas(self):
        return self.escenas  

    def getGrandeza(self):
        return self.grandezaParte     

#Clase Espectaculo    
class Espectaculo:
    def __init__(self):
        self.partes = []
        self.grandezaEspectaculo = 0

    def agregar_parte(self, parte):
        self.partes.append(parte)
        self.aumentar_grandeza(parte.grandezaParte)      

    def aumentar_grandeza(self, cantidad):
        self.grandezaEspectaculo += cantidad

    def getPartes(self):
        return self.partes

    def getGrandeza(self):
        return self.grandezaEspectaculo   

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
       

#Clase Arbol
class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None

    # Crea un árbol binario de búsqueda
    # Complejidad: O(n^2) en el caso de que el árbol tenga una altura de n
    def TREE_INSERT (self, nodo):
        y = None
        x = self.raiz
        #Mientras x no sea nulo, busca la posición del nodo
        while x != None:
            y = x
            if nodo.getValor().getGrandeza() < x.getValor().getGrandeza():
            # if nodo.getValor() < x.getValor():
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
        elif nodo.getValor().getGrandeza() < y.getValor().getGrandeza():
            y.setHijoIzq(nodo)
            nodo.setColor("RED")
        else:
            y.setHijoDer(nodo)
            nodo.setColor("RED")

        #Garantizar Arbol Rojo y Negro
        if nodo.getPadre() != None and nodo.getPadre().getPadre():
            self.insert_fixup(nodo)

    #Complejidad constante
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
            
    #Complejidad constante
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
            
    #Complejidad         
    def insert_fixup(self, nodo):
        while nodo != self.raiz and nodo.getPadre().getColor() == 'RED':
            if nodo.getPadre() == nodo.getPadre().getPadre().getHijoIzq():
                y = nodo.getPadre().getPadre().getHijoDer()
                if y is not None and y.getColor() == 'RED':
                    nodo.getPadre().setColor('BLACK')
                    y.setColor('BLACK')
                    nodo.getPadre().getPadre().setColor('RED')
                    nodo = nodo.getPadre().getPadre()
                else:
                    if nodo == nodo.getPadre().getHijoDer():
                        nodo = nodo.getPadre()
                        self.LEFT_ROTATE(nodo)
                    nodo.getPadre().setColor('BLACK')
                    nodo.getPadre().getPadre().setColor('RED')
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
        self.raiz.setColor('BLACK')
            
    def print_tree(self):
        self._print_tree_helper(self.raiz, "")

    def _print_tree_helper(self, nodo, prefix):
        if nodo is None:
            return

        color = nodo.getColor()
        if color is None:
            color = 'Desconocido'

        print(prefix + "├──", nodo.getValor().getGrandeza(), "(Color: " + color + ")")

        if nodo.getHijoIzq() is not None:
            self._print_tree_helper(nodo.getHijoIzq(), prefix + "│   ")
        
        if nodo.getHijoDer() is not None:
            self._print_tree_helper(nodo.getHijoDer(), prefix + "│   ")




    


    

















        
