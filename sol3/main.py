from entrada import leer_archivo
from clases import hallarRepeticion, imprimir_parte, imprimir_espectaculo, imprimir_escena
from time import time
import argparse

def main(filename):
    inicio = time()
    n, m, k, animales, apertura, espectaculo = leer_archivo(filename)
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
    fin = time()
    print("\n", "Tiempo de ejecución: ", round(fin-inicio,5), " segundos")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Nombre del archivo de entrada")
    args = parser.parse_args()
    main(args.filename)