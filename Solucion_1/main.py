from entrada import *
from clases import hallarRepeticion, imprimir_parte, imprimir_espectaculo, imprimir_escena
from time import time

def main():
    print("=========== APERTURA ==============")
    imprimir_parte(apertura)
    print("")
    print("=========== M-1 Partes ==============")
    imprimir_espectaculo(espectaculo)

    print("")
    print("=========== DATOS PUNTUALES SOLICITADOS ==============")
    print("")
    lista, repeticiones = hallarRepeticion(False)
    print("Los animales que participaron en menos escenas fueron: ", lista)
    print("Las escenas en las que participaron fueron: ", repeticiones)

    print("")
    lista, repeticiones = hallarRepeticion(True)
    print("Los animales que participaron en más escenas fueron: ", lista)
    print("Las escenas en las que participaron fueron: ", repeticiones)

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