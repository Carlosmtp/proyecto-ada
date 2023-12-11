# # Lista de animales existentes
# animales_existentes = [
# "Capibara",
# "Loro",
# "Caiman",
# "Boa",
# "Cocodrilo",
# "Cebra",
# "Panteranegra",
# "Tigre",
# "Leon",
# "Elefante",
# "Jirafa",
# "Hipopotamo",
# "Rinoceronte",
# "Oso",
# "Zorro",
# "Ardilla",
# "Castor",
# "Conejo",
# "Ciervo",
# "Oveja",
# "Cabra",
# "Cerdo",
# "Vaca",
# "Toro",
# "Perro",
# "Gato",
# "Pato",
# "Gallina",
# "Pavo",
# "Pajaro"]

# # Generar nuevos animales
# nuevos_animales = []
# for i in range(1001, 2001):
#     animal = f"Animal{i}"
#     if animal not in animales_existentes:
#         nuevos_animales.append((animal, i))

# # Imprimir los nuevos animales
# for animal, i in nuevos_animales:
#     print(f"{animal} {i}")

from itertools import combinations

# Generar una lista de 2000 animales
animales = [f"Animal{i}" for i in range(1, 50)]

# Generar todas las combinaciones posibles de tres animales
combinaciones = list(combinations(animales, 3))

# Seleccionar las primeras 2000 combinaciones
combinaciones_seleccionadas = combinaciones[:30000]

# Abrir el archivo en modo de escritura
with open('combinaciones.txt', 'w') as f:
    # Escribir las combinaciones seleccionadas en el archivo
    for combinacion in combinaciones_seleccionadas:
        f.write(' '.join(combinacion) + '\n')
    