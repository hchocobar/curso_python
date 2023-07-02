# Encontrar el mayor valor en la lista.
# El concepto es bastante simple: asumimos temporalmente que el primer elemento es el más grande y comparamos la
# hipótesis con todos los elementos restantes de la lista.

# Ejemplo 1 - for range
mi_lista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = mi_lista[0]
for i in range(1, len(mi_lista)):
    if mi_lista[i] > mayor:
        mayor = mi_lista[i]
print("Utilizando for range:", mayor)

# Ejemplo 2 - for in
mi_lista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = mi_lista[0]
for i in mi_lista:
    if i > mayor:
        mayor = i
print("Utilizando for in:", mayor)

# Ejemplo 3 - utilizando rodajas
mi_lista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = mi_lista[0]
for i in mi_lista[1:]:
    if i > mayor:
        mayor = i
print("Utilizando rodajas:", mayor)
