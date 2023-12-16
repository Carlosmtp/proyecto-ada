import argparse
class Pila:

  def __init__(self):
    self.items = []

  def esta_vacia(self):
    return len(self.items) == 0

  def apilar(self, elemento):
    self.items.append(elemento)

  def desapilar(self):
    if not self.esta_vacia():
      return self.items.pop()
    else:
      print("La pila está vacía")

  def ver_tope(self):
    if not self.esta_vacia():
      return self.items[-1]
    else:
      print("La pila está vacía")

  def ver_pila(self):
    return self.items


def leer_archivo(filename):
  n = 0
  m = 0
  k = 0
  pilaAnimales = Pila()
  pilaApertura = Pila()
  pilaPartes = Pila()

  with open(filename, 'r') as file:
    n, m, k = map(int, file.readline().split())
    file.readline()
    for i in range(n):
      linea = file.readline().strip().split()
      animal = linea[0]
      grandeza = int(linea[1])
      pilaAnimales.apilar((animal, grandeza))
    file.readline()
    for i in range((m - 1) * k):
      linea = file.readline().strip().split()
      animal1 = linea[0]
      animal2 = linea[1]
      animal3 = linea[2]
      pilaApertura.apilar((animal1, animal2, animal3))
    file.readline().split()
    for i in range(m - 1):
      pilaParte = Pila()
      for j in range(k):
        linea = file.readline().strip().split()
        animal1 = linea[0]
        animal2 = linea[1]
        animal3 = linea[2]
        pilaParte.apilar((animal1, animal2, animal3))
      pilaPartes.apilar(pilaParte)

  return n, m, k, pilaAnimales, pilaApertura, pilaPartes


def dividir_y_agrupar_pila(original, x):
  # Crear una lista de pilas para almacenar las partes
  pilas_partes = [Pila() for _ in range(x)]

  # Contar la cantidad total de elementos en la pila original
  total_elementos = 0
  pila_temporal = Pila()
  while not original.esta_vacia():
    elemento = original.desapilar()
    pila_temporal.apilar(elemento)
    total_elementos += 1

  # Dividir los elementos en n partes
  elementos_por_parte = total_elementos // x
  for pila_parte in pilas_partes:
    for _ in range(elementos_por_parte):
      elemento = pila_temporal.desapilar()
      pila_parte.apilar(elemento)

  # Almacenar los elementos restantes en la última pila si es necesario
  while not pila_temporal.esta_vacia():
    pilas_partes[-1].apilar(pila_temporal.desapilar())

  # Crear una pila de pilas
  pila_de_pilas = Pila()
  for pila_parte in reversed(pilas_partes):
    pila_de_pilas.apilar(pila_parte)

  return pila_de_pilas

def max(conteo_animales):
  if not conteo_animales:
      return None
  
  max_frecuencia = float('-inf')
  
  for frecuencia in conteo_animales.values():
      if frecuencia > max_frecuencia:
          max_frecuencia = frecuencia
  
  return max_frecuencia
  
def min(conteo_animales):
  if not conteo_animales:
      return None
  
  min_frecuencia = float('inf')
  
  for frecuencia in conteo_animales.values():
      if frecuencia < min_frecuencia:
          min_frecuencia = frecuencia
  
  return min_frecuencia


def mayorParticipacion(pilaApertura):
  # Crear una copia de la pila original para evitar modificarla
  pila_copiaAp = Pila()
  pila_copiaP = Pila()

  while not pilaApertura.esta_vacia():
    animal1, animal2, animal3 = pilaApertura.desapilar()
    pila_copiaAp.apilar((animal1, animal2, animal3))

  # Contar la frecuencia de cada animal en la copia de la pilaApertura
  conteo_animales = {}
  while not pila_copiaAp.esta_vacia():
    animal1, animal2, animal3 = pila_copiaAp.desapilar()

    for animal in (animal1, animal2, animal3):
      conteo_animales[animal] = conteo_animales.get(animal, 0) + 1

    # Volver a apilar los elementos en la pila original
    pilaApertura.apilar((animal1, animal2, animal3))

  if not conteo_animales:
    # No hay animales en las pilas originales.
    return None

  # Multiplicar el conteo por dos para contar su participación en las partes
  conteo_animales = {animal: conteo * 2 for animal, conteo in conteo_animales.items()}
  

  # Encontrar la frecuencia mínima
  frecuencia_maxima = max(conteo_animales)

  print(frecuencia_maxima)

  # Encontrar todos los animales con la frecuencia mínima
  animales_mas_repetidos = [
      animal for animal, frecuencia in conteo_animales.items()
      if frecuencia == frecuencia_maxima
  ]

  #print(pilaPartes.ver_pila())
  return animales_mas_repetidos


def menorParticipacion(pilaApertura):
  # Crear una copia de la pila original para evitar modificarla
  pila_copia = Pila()
  while not pilaApertura.esta_vacia():
    animal1, animal2, animal3 = pilaApertura.desapilar()
    pila_copia.apilar((animal1, animal2, animal3))

  # Contar la frecuencia de cada animal en la copia de la pilaApertura
  conteo_animales = {}
  while not pila_copia.esta_vacia():
    animal1, animal2, animal3 = pila_copia.desapilar()

    for animal in (animal1, animal2, animal3):
      conteo_animales[animal] = conteo_animales.get(animal, 0) + 1

    # Volver a apilar los elementos en la pila original
    pilaApertura.apilar((animal1, animal2, animal3))

  if not conteo_animales:
    # No hay animales en las pilas originales.
    return None

  # Multiplicar el conteo por dos para contar su participación en las partes
  conteo_animales = {animal: conteo * 2 for animal, conteo in conteo_animales.items()}
  
  # Encontrar la frecuencia mínima
  frecuencia_minima = min(conteo_animales)

  # Encontrar todos los animales con la frecuencia mínima
  animales_menos_repetidos = [
      animal for animal, frecuencia in conteo_animales.items()
      if frecuencia == frecuencia_minima
  ]

  return animales_menos_repetidos


def mayorGrandeza(pilaAnimales, pilaApertura):
  suma_maxima = float('-inf')  # Inicializar con un valor muy bajo
  elemento_maximo = None
  
  def calcular_suma(tripleta):
      return sum(grandeza for animal, grandeza in pilaAnimales.ver_pila() if animal in tripleta)
  
  # Crear una copia de pilaApertura para evitar modificar la original
  pila_apertura_copia = Pila()
  
  while not pilaApertura.esta_vacia():
      tripleta = pilaApertura.desapilar()
      pila_apertura_copia.apilar(tripleta)  # Apilar en la copia
      suma_actual = calcular_suma(tripleta)
  
      if suma_actual > suma_maxima:
          suma_maxima = suma_actual
          elemento_maximo = tripleta
  
  # Restaurar la pilaApertura con la copia
  while not pila_apertura_copia.esta_vacia():
      pilaApertura.apilar(pila_apertura_copia.desapilar())
  
  return elemento_maximo


def menorGrandeza(pilaAnimales, pilaApertura):
  suma_minima = float('inf')  # Inicializar con un valor muy alto
  elemento_minimo = None

  def calcular_suma(tripleta):
    return sum(grandeza for animal, grandeza in pilaAnimales.ver_pila()
               if animal in tripleta)

  # Crear una copia de pilaApertura para evitar modificar la original
  pila_apertura_copia = Pila()

  while not pilaApertura.esta_vacia():
    tripleta = pilaApertura.desapilar()
    pila_apertura_copia.apilar(tripleta)  # Apilar en la copia
    suma_actual = calcular_suma(tripleta)

    if suma_actual < suma_minima:
      suma_minima = suma_actual
      elemento_minimo = tripleta

  # Restaurar la pilaApertura con la copia
  while not pila_apertura_copia.esta_vacia():
      pilaApertura.apilar(pila_apertura_copia.desapilar())

  return elemento_minimo

def Promedio(pilaAnimales, pilaApertura):
  suma_total = 0

  # Crear una copia de pilaApertura para evitar modificar la original
  pila_apertura_copia = Pila()

  while not pilaApertura.esta_vacia():
      tripleta = pilaApertura.desapilar()
      pila_apertura_copia.apilar(tripleta)  # Apilar en la copia

      # Calcular la suma de grandezas para la tripleta actual
      suma_tripleta = sum(grandeza for animal, grandeza in pilaAnimales.ver_pila() if animal in tripleta)

      suma_total += suma_tripleta

  # Restaurar la pilaApertura con la copia
  while not pila_apertura_copia.esta_vacia():
      pilaApertura.apilar(pila_apertura_copia.desapilar())

  return (suma_total)/((m-1)*k)

def ordenarApertura(pilaAnimales, pilaApertura):
    # Crear una lista temporal para almacenar las tripletas junto con su suma de grandezas
    tripletas_con_suma = []

    # Crear una copia de la pila original para evitar modificarla
    pilaApertura_copia = Pila()

    # Calcular la suma de grandezas para cada tripleta y almacenarla en la lista temporal
    while not pilaApertura.esta_vacia():
        tripleta = pilaApertura.desapilar()
        pilaApertura_copia.apilar(tripleta)  # Apilar en la copia
        suma_tripleta = sum(grandeza for animal, grandeza in pilaAnimales.ver_pila() if animal in tripleta)
        tripletas_con_suma.append((tripleta, suma_tripleta))

    # Restaurar la pila original con la copia
    while not pilaApertura_copia.esta_vacia():
        pilaApertura.apilar(pilaApertura_copia.desapilar())

    # Ordenar la lista temporal por la suma de grandezas en orden ascendente
    tripletas_con_suma.sort(key=lambda x: x[1])

    # Crear una nueva pila ordenada
    pila_ordenada = Pila()

    # Apilar las tripletas ordenadas en la pila ordenada
    for tripleta, _ in tripletas_con_suma:
        pila_ordenada.apilar(tripleta)

    return pila_ordenada

def ordenarPartes(pilaAnimales, pilaPartes):
  # Crear una lista temporal para almacenar todas las tripletas con su suma de grandezas
  lista_con_suma = []

  # Procesar cada pila de tripletas en pilaPartes
  while not pilaPartes.esta_vacia():
      pila_parte = pilaPartes.desapilar()

      # Calcular la suma de grandezas para cada tripleta y almacenarla en la lista temporal
      while not pila_parte.esta_vacia():
          tripleta = pila_parte.desapilar()
          suma_tripleta = sum(grandeza for animal, grandeza in pilaAnimales.ver_pila() if animal in tripleta)
          lista_con_suma.append((tripleta, suma_tripleta))

  # Ordenar la lista temporal por la suma de grandezas en orden ascendente
  lista_con_suma.sort(key=lambda x: x[1])

  # Crear una nueva pila para almacenar las tripletas ordenadas
  pila_ordenada = Pila()

  # Apilar las tripletas ordenadas en la pila
  for tripleta, _ in lista_con_suma:
      pila_ordenada.apilar(tripleta)
      pilaPartes.apilar(tripleta)

  return pila_ordenada




#Print final con los datos ordenados

def main(filename):
  global n, m, k, animales, apertura, partes
  n, m, k, animales, apertura, partes = leer_archivo(filename) 
  

  min_participacion = menorParticipacion(apertura)
  print("Animal con menor participacion:\n", min_participacion,"\n")
  
  max_participacion = mayorParticipacion(apertura)
  print("Animal con mayor participacion:\n", max_participacion,"\n")
  
  escena_menor_grandeza = menorGrandeza(animales,apertura)
  print("Escena con menor grandeza:\n", escena_menor_grandeza,"\n")

  escena_mayor_grandeza = mayorGrandeza(animales,apertura)
  print("Escena con mayor grandeza:\n", escena_mayor_grandeza,"\n")
  
  ordenar_apertura = (ordenarApertura(animales,apertura)).ver_pila()
  print("Apertura ordenada ascendentemente:\n",ordenar_apertura,"\n")

  ordenar_partes = (ordenarPartes(animales,partes)).ver_pila()
  print("Partes ordenadas ascendentemente:\n",ordenar_partes,"\n")

  promedio = Promedio(animales, apertura)
  print("Promedio de grandeza:\n", promedio)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Nombre del archivo de entrada")
    args = parser.parse_args()
    main(args.filename)