from clases import Animal, Escena, Parte, Espectaculo

# Complejidad: O(N) donde N es el número de líneas en el archivo
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
        #Crear objetos de animales y almacenarlos en un diccionario
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






