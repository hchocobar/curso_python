# Ejemplo 1 - función range() con un parámetro inicia desde 0
for i in range(10):  # rango((p1), p2, (p3))
    print("El valor de i del Ejemplo 1 es actualmente", i)
print()

# Ejemplo 2 - función range() con dos parámetros
for i in range(5, 10):
    print("El valor de i del Ejemplo 2 es actualmente", i)
print()

# Ejemplo 3 - función range() con tres parámetros, el incremento
for i in range(2, 18, 2):
    print("El valor de i es actualmente", i)
print()

# Ejemplo 4
potencia = 1
for exp in range(1, 10):
    print("2 a la potencia de", exp, "es", potencia)
    potencia *= 2
