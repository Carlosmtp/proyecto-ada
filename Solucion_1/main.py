from entrada import *
from clases import INORDER_PARTE, INORDER_ESCENAS

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
    print("El/Los animal(es) que participó/participaron en más escenas fue: ")

    print("El/Los animal(es) que participó/participaron en menos escenas fue: ")

    print("")
    print("La escena de mayor grandeza total fue: ")
    INORDER_ESCENAS(apertura.getEscenas().TREE_MAXIMUM().getAnimales().getRaiz())

    print("")
    print("La escena de menor grandeza total fue: ")
    INORDER_ESCENAS(apertura.getEscenas().TREE_MINIMUN().getAnimales().getRaiz())

    print("El promedio de grandeza de todo el espectaculo fue: ")
    espectaculo.getGrandeza()

    # INORDER_TREE_WALK(escena1.getAnimales().getRaiz())


main()