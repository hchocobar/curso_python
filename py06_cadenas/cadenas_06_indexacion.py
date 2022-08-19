# las cadenas son secuencias (no listas) y podemos recorrerlas utilizando su indice
cadena = 'dando la vuelta del perro'
#         0123456789012345678901234

for i in range(len(cadena)):  # range(start, stop (no include), step)
    print(cadena[i], end=' ')
print()

# Iterando a través de una cadena con el operador in
for ch in cadena:
    print(ch, end=' ')
print()
