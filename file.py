# Genera animales diferentes
# # Abrir el archivo en modo de escritura
# with open("animales.txt", "w") as archivo:
#     # Bucle para generar 50 animales
#     for i in range(1, 50):
#         # Generar el nombre del animal
#         animal = f"Animal{i}"
#         # Escribir el animal y el número en el archivo
#         archivo.write(f"{animal} {i}\n")

# Genera escenas diferentes
# from itertools import combinations

# # Generar una lista de 2000 animales
# animales = [f"Animal{i}" for i in range(1, 50)]

# # Generar todas las combinaciones posibles de tres animales
# combinaciones = list(combinations(animales, 3))

# # Seleccionar las primeras 2000 combinaciones
# combinaciones_seleccionadas = combinaciones[:15000]

# # Abrir el archivo en modo de escritura
# with open('combinaciones.txt', 'w') as f:
#     # Escribir las combinaciones seleccionadas en el archivo
#     for combinacion in combinaciones_seleccionadas:
#         f.write(' '.join(combinacion) + '\n')