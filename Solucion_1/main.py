from entrada import *
from clases import INORDER_PARTE, INORDER_ESCENAS, hallarRepeticion

def main():
    print("=========== APERTURA ==============")
    INORDER_PARTE(apertura.getEscenas().getRaiz())
    print("=========== Parte 1 ==============")
    INORDER_PARTE(parte1.getEscenas().getRaiz())
    print("=========== Parte 2 ==============")
    INORDER_PARTE(parte2.getEscenas().getRaiz())

    print("")
    print("=========== DATOS PUNTUALES SOLICITADOS ==============")
    print("")
    diccionario = {}
    print("Los animales que participaron en más escenas fueron: ", hallarRepeticion(apertura.getEscenas().getRaiz(), diccionario, True))

    print("Los animales que participaron en menos escenas fueron: ", hallarRepeticion(apertura.getEscenas().getRaiz(), diccionario, False))

    print("")
    print("La escena de mayor grandeza total fue: ")
    INORDER_ESCENAS(apertura.getEscenas().TREE_MAXIMUM().getAnimales().getRaiz())

    print("")
    print("La escena de menor grandeza total fue: ")
    INORDER_ESCENAS(apertura.getEscenas().TREE_MINIMUN().getAnimales().getRaiz())

    print("El promedio de grandeza de todo el espectaculo fue: ")
    print(espectaculo.getPromedioGrandeza())


main()