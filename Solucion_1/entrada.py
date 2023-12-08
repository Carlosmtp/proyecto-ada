from clases import Animal, Escena, Parte, ArbolBinarioBusqueda, Nodo

# Datos de entrada
# n=6, m=3, k=2
# Crear objetos de animales
animal1 =  Nodo(Animal("León", 6))
animal2 =  Nodo(Animal("Elefante", 3))
animal3 =  Nodo(Animal("Tigre", 1))
animal4 =  Nodo(Animal("Jirafa", 5))
animal5 =  Nodo(Animal("Cebra", 4))
animal6 =  Nodo(Animal("Hipopótamo", 2))

# Crear objetos de escenas
escena1 = Escena()
escena1.agregar_animal(animal1)
escena1.agregar_animal(animal2)
escena1.agregar_animal(animal3)
print(escena1.getAnimales())
# escena2 = Escena()
# escena2.agregar_animal(animal4)
# escena2.agregar_animal(animal6)
# escena2.agregar_animal(animal5)
# escena3 = Escena()
# escena3.agregar_animal(animal1)
# escena3.agregar_animal(animal6)
# escena3.agregar_animal(animal3)
# escena4 = Escena()
# escena4.agregar_animal(animal2)
# escena4.agregar_animal(animal1)
# escena4.agregar_animal(animal5)

# apertura = Parte()
# apertura.agregar_escena(escena1)
# apertura.agregar_escena(escena2)
# apertura.agregar_escena(escena3)
# apertura.agregar_escena(escena4)

# parte1 = Parte()
# parte1.agregar_escena(escena4)
# parte1.agregar_escena(escena3)

# parte2 = Parte()
# parte2.agregar_escena(escena2)
# parte2.agregar_escena(escena1)

# print('La grandeza total es: ', escena2.getGrandeza())
# print('La grandeza total es: ', escena1.getGrandeza())
# print('La grandeza total es: ', parte2.getGrandeza())

# Crear Objeto Arbol
arbol = ArbolBinarioBusqueda()

nodo1 = Nodo(escena1)
nodo2 = Nodo(escena2)
nodo3 = Nodo(escena3)
nodo4 = Nodo(escena4)
# nodo5 = Nodo(6)
# nodo6 = Nodo(6)
# nodo7 = Nodo(7)
# nodo8 = Nodo(8)
# nodo9 = Nodo(9)
# nodo10 = Nodo(10)

arbol.TREE_INSERT(nodo1)
arbol.TREE_INSERT(nodo2)
arbol.TREE_INSERT(nodo3)
arbol.TREE_INSERT(nodo4)
# arbol.TREE_INSERT(nodo5)
# arbol.TREE_INSERT(nodo6)
# arbol.TREE_INSERT(nodo7)
# arbol.TREE_INSERT(nodo8)
# arbol.TREE_INSERT(nodo9)
# arbol.TREE_INSERT(nodo10)

arbol.print_tree()