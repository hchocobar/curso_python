# Encontrar el mayor valor en la lista.
# El concepto es bastante simple: asumimos temporalmente que el primer elemento es el más grande y comparamos la
# hipótesis con todos los elementos restantes de la lista.

# Ejemplo 1 - for range
miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista[0]

for i in range(1, len(miLista)):
   if miLista [i]> mayor:
        mayor = miLista[i]

print("\nUtilizando for range", mayor)

# Ejemplo 2 - for in
miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista [0]

for i in miLista:
    if i > mayor:
        mayor = i

print("\nUtilizando for in: ", mayor)

# Ejemplo 3 - utilizando rodajas
miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista [0]

for i in miLista [1:]:
   if i > mayor:
        mayor = i

print("\nUtilizando Rodajas: ", mayor)
