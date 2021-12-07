# Ejemplo 1 - navegar a través de los elementos de una tupla con un bucle
print('ejemplo 1')
tup1 = (1, 2, 3)
for elem in tup1:
    print(elem)  # probar operaciones dentro del print

# Ejemplo 2 - verificar si un elemento o no esta presente en la tupla utilizando los operadores in / not in
print('ejemplo 2')
tup2 = (1, 2, 3, 4)
print(5 in tup2)
print(5 not in tup2)

# Ejemplo 3 - emplear la función len() para verificar cuantos elementos existen en la tupla
print('ejemplo 3')
tup3 = (1, 2, 3, 4, 5, 6)
print(len(tup3))

# Ejemplo 4 - incluso unir o multiplicar tuplas
print('ejemplo 4')
tup4 = tup1 + tup2
tup5 = tup3 * 2
print(tup4)
print(type(tup4))
print(tup5)
print(type(tup5))
