from time import time
import argparse

def leer_archivo(filename):
    n=0
    m=0
    k=0
    animales = {} 
    apertura = [] 
    partes = [] 
    with open(filename, 'r') as file:
        n, m, k = map(int, file.readline().split())
        file.readline()
        for i in range(n):
            animal, grandeza = file.readline().strip().split()
            animales[animal] = int(grandeza)
        file.readline().split()
        for i in range((m-1)*k):
            apertura.append(file.readline().strip().split())
        file.readline().split()
        for i in range(m-1):
            parte = []
            for j in range(k):
                parte.append(file.readline().strip().split())
            partes.append(parte)
    return n, m, k, animales, apertura, partes

def participacion_animales(apertura):
    participacion = {}
    for i in range((m-1)*k):
        for j in range(3):
            if apertura[i][j] in participacion:
                participacion[apertura[i][j]] += 2
            else:
                participacion[apertura[i][j]] = 2
    return participacion

def animal_mas_menos_participacion(participaciones):
    animal_mas_participacion = []
    animal_menos_participacion = []
    max = 0
    min = float('inf')
    for i in participaciones:
        if participaciones[i] > max:
            max = participaciones[i]
        if participaciones[i] < min:
            min = participaciones[i]
    for i in participaciones:
        if participaciones[i] == max:
            animal_mas_participacion.append(i)
        if participaciones[i] == min:
            animal_menos_participacion.append(i)
    return animal_menos_participacion, min, animal_mas_participacion, max

def ordenarEscena(escena,grandezas):
    grandeza=0
    for i in range(3):
        grandeza+=grandezas[escena[i]]
    for i in range(2):
        for j in range(2):
            if grandezas[escena[j]]>grandezas[escena[j+1]]:
                aux=escena[j]
                escena[j]=escena[j+1]
                escena[j+1]=aux
            elif grandezas[escena[j]]==grandezas[escena[j+1]]:
                if escena[j]>escena[j+1]:
                    aux = escena[j]
                    escena[j] = escena[j + 1]
                    escena[j + 1] = aux
    return escena, grandeza

def ordenarParte(parte, grandezas, isApertura):
    grandeza=0
    if isApertura:
        long = (m-1)*k
    else:
        long = k
    for i in range(long):
        parte[i] = ordenarEscena(parte[i], grandezas)
        grandeza+=parte[i][1]
    for i in range(long - 1):
        for j in range(long - 1):
            if parte[j][1] > parte[j + 1][1]:
                aux = parte[j]
                parte[j] = parte[j + 1]
                parte[j + 1] = aux
            elif parte[j][1] == parte[j + 1][1]:
                if grandezas[parte[j][0][2]] > grandezas[parte[j + 1][0][2]]:
                    aux = parte[j]
                    parte[j] = parte[j + 1]
                    parte[j + 1] = aux
    return parte, grandeza

def ordenarPartes(partes, grandezas):
    grandeza=0
    for i in range(m-1):
        partes[i]=ordenarParte(partes[i],grandezas,False)
        grandeza+=partes[i][1]
    for i in range(m-2):
        for j in range(m-2):
            if partes[j][1]>partes[j+1][1]:
                aux=partes[j]
                partes[j]=partes[j+1]
                partes[j+1]=aux
            elif partes[j][1]==partes[j+1][1]:
                if partes[j][0][k-1][1]>partes[j+1][0][k-1][1]:
                    aux=partes[j]
                    partes[j]=partes[j+1]
                    partes[j+1]=aux
    return partes

def promedio_grandeza(apertura):
    return apertura[1]/((m-1)*k)

def main(filename):
    inicio = time()
    global n, m, k, animales, apertura, partes
    n, m, k, animales, apertura, partes = leer_archivo(filename)
    participaciones=participacion_animales(apertura)
    apertura_sorted = ordenarParte(apertura, animales, True)
    print("Apertura:\n", apertura_sorted,"\n")
    partes_sorted = ordenarPartes(partes, animales)
    print("Partes:\n", partes_sorted,"\n")
    min_max_participacion = animal_mas_menos_participacion(participaciones)
    print("Animal con menor participacion:\n", min_max_participacion[0], "\nCantidad de participaciones:", min_max_participacion[1], "\n")
    print("Animal con mayor participacion:\n", min_max_participacion[2], "\nCantidad de participaciones:", min_max_participacion[3], "\n")
    escena_menor_grandeza = apertura_sorted[0][0]
    print("Escena menor grandeza:\n", escena_menor_grandeza,"\n")
    escena_mayor_grandeza = apertura_sorted[0][(m-1)*k-1]
    print("Escena mayor grandeza:\n", escena_mayor_grandeza,"\n")
    promedio = promedio_grandeza(apertura_sorted)
    print("Promedio de grandeza:\n", round(promedio,2))
    fin = time()
    print("\n","Tiempo de ejecución: ", round(fin-inicio,5), " segundos")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Nombre del archivo de entrada")
    args = parser.parse_args()
    main(args.filename)