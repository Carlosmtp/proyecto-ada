from clases import Animal, Escena, Parte, Espectaculo

# Datos de entrada
# n=6, m=3, k=2
# Crear objetos de animales
animal1 = Animal("León", 6)
animal2 = Animal("Elefante", 3)
animal3 = Animal("Tigre", 1)
animal4 = Animal("Jirafa", 5)
animal5 = Animal("Cebra", 4)
animal6 = Animal("Hipopótamo", 2)

# Crear objetos de escenas
escena1 = Escena()
escena1.agregar_animal(animal1)
escena1.agregar_animal(animal2)
escena1.agregar_animal(animal3)
# escena1.printAnimales()

escena2 = Escena()
escena2.agregar_animal(animal4)
escena2.agregar_animal(animal3)
escena2.agregar_animal(animal5)
# escena2.printAnimales()

escena3 = Escena()
escena3.agregar_animal(animal1)
escena3.agregar_animal(animal6)
escena3.agregar_animal(animal3)
# escena3.printAnimales()

escena4 = Escena()
escena4.agregar_animal(animal2)
escena4.agregar_animal(animal1)
escena4.agregar_animal(animal5)
# escena4.printAnimales()

apertura = Parte()
apertura.agregar_escena(escena1)
apertura.agregar_escena(escena2)
apertura.agregar_escena(escena3)
apertura.agregar_escena(escena4)
# apertura.printEscenas()

# # Debe ser modificado en lugar de la grandeza se debe arrojar la escena
# print('La escena con mayor grandeza fue: ', apertura.getEscenas().TREE_MAXIMUM())
# print('La escena con menor grandeza fue:', apertura.getEscenas().TREE_MINIMUN())

parte1 = Parte()
parte1.agregar_escena(escena4)
parte1.agregar_escena(escena3)
# parte1.getEscenas()

parte2 = Parte()
parte2.agregar_escena(escena2)
parte2.agregar_escena(escena1)
# parte2.getEscenas()

#Espectaculo
espectaculo = Espectaculo()
espectaculo.agregar_parte(apertura)
espectaculo.agregar_parte(parte1)
espectaculo.agregar_parte(parte2)

