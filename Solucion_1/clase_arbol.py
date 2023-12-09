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
        #Mientras x no sea nulo, busca la posición del nodo
        while x != None:
            y = x
            if nodo.getValor().getGrandeza() < x.getValor().getGrandeza():
                x = x.getHijoIzq()
            # elif nodo.getValor().getGrandeza() == x.getValor().getGrandeza() and isinstance(nodo.getValor(),Escena) and isinstance(x.getValor(),Escena):  
            #     if nodo.getValor().getAnimales().TREE_MAXIMUM().getGrandeza() < x.getValor().getAnimales().TREE_MAXIMUM().getGrandeza():
            #         x = x.getHijoIzq()
            #     else:
            #         x = x.getHijoDer()
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

