from entrada import *
from clases import hallarRepeticion, imprimir_parte, imprimir_espectaculo, imprimir_escena

def main():
    print("=========== APERTURA ==============")
    imprimir_parte(apertura)
    print("=========== M-1 Partes ==============")
    imprimir_espectaculo(espectaculo)

    print("")
    print("=========== DATOS PUNTUALES SOLICITADOS ==============")
    print("")
    diccionario = {}
    # print(partes)
    print("Los animales que participaron en más escenas fueron: ", 
          hallarRepeticion(apertura, diccionario, True))
    # print("Los animales que participaron en menos escenas fueron: ", 
    #       hallarRepeticion(espectaculo, diccionario, False))

    print("")
    print("La escena de mayor grandeza total fue: ")
    imprimir_escena(apertura.getEscenas().TREE_MAXIMUM())

    print("")
    print("La escena de menor grandeza total fue: ")
    imprimir_escena(apertura.getEscenas().TREE_MINIMUN())

    print("")
    print("El promedio de grandeza de todo el espectaculo fue: ")
    print(apertura.getPromedioGrandeza())

main()