# Las cadenas son secuencias (no listas) y podemos recorrerlas utilizando su índice
cadena = 'dando la vuelta del perro'
#         0123456789012345678901234

for i in range(len(cadena)):  # Sintaxis: range(start, stop (no include), step)
    print(cadena[i], end=' ')  # Salida: d a n d o   l a   v u e l t a   d e l   p e r r o
print()

# Iterando a través de una cadena con el operador in
for ch in cadena:
    print(ch, end=' ')  # Salida: d a n d o   l a   v u e l t a   d e l   p e r r o
print()
