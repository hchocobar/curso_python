# Encontrar el mayor valor en la lista.
mi_lista = [17, 3, 11, 5, 1, 9, 7, 15, 13]


# El concepto es bastante simple: asumimos temporalmente que el primer elemento es el más grande y comparamos la
# hipótesis con todos los elementos restantes de la lista.
mayor = mi_lista[0]

# Ejemplo 1 - for range
for i in range(1, len(mi_lista)):
    if mi_lista[i] > mayor:
        mayor = mi_lista[i]

print("\nUtilizando for range", mayor)

# Ejemplo 2 - for in
mi_lista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = mi_lista[0]

for i in mi_lista:
    if i > mayor:
        mayor = i

print("\nUtilizando for in: ", mayor)

# Ejemplo 3 - utilizando rodajas
mi_lista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = mi_lista[0]

for i in mi_lista[1:]:
    if i > mayor:
        mayor = i

print("\nUtilizando Rodajas: ", mayor)
