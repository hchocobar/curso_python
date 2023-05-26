# Ejemplo 1 - navegar a través de los elementos de una tupla con un bucle
print('Ejemplo 1')
mi_tupla1 = (1, 2, 3)
for element in mi_tupla1:
    print(element)  # probar operaciones dentro del print

# Ejemplo 2 - verificar si un elemento o no está presente en la tupla utilizando los operadores in / not in
print('Ejemplo 2')
mi_tupla2 = (1, 2, 3, 4)
print(5 in mi_tupla2)  # Salida: False
print(5 not in mi_tupla2)  # Salida: True

# Ejemplo 3 - emplear la función len() para verificar cuantos elementos existen en la tupla
print('Ejemplo 3')
mi_tupla3 = (1, 2, 3, 4, 5, 6)
print(len(mi_tupla3))  # Salida: 6

# Ejemplo 4 - incluso unir o multiplicar tuplas
print('Ejemplo 4')
mi_tupla4 = mi_tupla1 + mi_tupla2
mi_tupla5 = mi_tupla3 * 2
print(mi_tupla4)  # Salida: (1, 2, 3, 1, 2, 3, 4)
print(type(mi_tupla4))  # Salida: <class 'tuple'>
print(mi_tupla5)  # Salida: (1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)
print(type(mi_tupla5))  # Salida: <class 'tuple'>
