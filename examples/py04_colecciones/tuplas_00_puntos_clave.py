# 1. Las Tuplas son colecciones de datos ordenadas e inmutables.
# Se puede pensar en ellas como listas inmutables.
# Se definen con paréntesis:
mi_tupla = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
print(mi_tupla)

meses = ('enero', 'febrero', 'marzo')

mi_lista = [1, 2, True, "una cadena", (3, 4), [5, 6], None]
print(mi_lista)

# Cada elemento de la tupla puede ser de un tipo de dato diferente (por ejemplo, enteros, cadenas, boleanos, etc.)
# Las tuplas pueden contener otras tuplas o listas (y viceversa).

# 2. Se puede crear una tupla vacía de la siguiente manera:
tupla_vacia = ()

print(type(tupla_vacia))  # Salida: <class 'tuple'>

# 3. La tupla de un solo elemento se puede definir de dos maneras:
tupla_un_elemento = ("uno",)  # Paréntesis y coma
tupla_un_elemento2 = "uno",  # Sin paréntesis, solo la coma

# Si eliminas la coma, Python creará una variable (no una tupla)
mi_tupla1 = 1,
print(type(mi_tupla1))  # Salida: <class 'tuple'>
mi_tupla2 = 1
print(type(mi_tupla2))  # Salida: <class 'int'>

# 4. Se pueden acceder los elementos de la tupla al indexarlos:
mi_tupla = (1, 2.0, "cadena", [3, 4], (5,), True)
print(mi_tupla[3])  # Salida: [3, 4]

# 5. Las tuplas son inmutables, lo que significa que no se puede agregar, modificar, cambiar o quitar elementos.
# El siguiente fragmento de código # provocará una excepción:
mi_tupla = (1, 2.0, "cadena", [3, 4], (5,), True)
# mi_tupla[2] = "guitarra"  # Se levanta una excepción TypeError

# Sin embargo, se puede eliminar la tupla completa:
mi_tupla = (1, 2, 3)
del mi_tupla
# print(mi_tupla)  # NameError: name 'mi_tupla' is not defined

# 6. Puedes navegar a través de los elementos de una tupla con un bucle
# Ejemplo 1 - verificar si un elemento o no está presente en la tupla
t1 = (1, 2, 3)
for element in t1:
    print(element)

# Ejemplo 2
t2 = (1, 2, 3, 4)
print(5 in t2)  # Salida: False
print(5 not in t2)  # Salida: True

# Ejemplo 3 - emplear la función len() para verificar cuantos elementos existen en la tupla
t3 = (1, 2, 3, 5)
print(len(t3))  # Salida: 4

# Ejemplo 4 - incluso unir o multiplicar tuplas
t4 = t1 + t2
t5 = t3 * 2
print(t4)  # Salida: (1, 2, 3, 1, 2, 3, 4)
print(t5)  # Salida: (1, 2, 3, 5, 1, 2, 3, 5)

# EXTRA
# También se puede crear una tupla utilizando la función integrada de Python tuple().
# Esto es particularmente útil cuando se desea convertir un iterable en una tupla
# (por ejemplo, una lista, rango, cadena, etcétera):
mi_tupla = tuple((1, 2, "cadena"))
print(mi_tupla)  # Salida: (1, 2, 'cadena')
mi_lista = [2, 4, 6]
print(mi_lista)  # Salida: [2, 4, 6]
print(type(mi_lista))  # Salida: <class 'list'>
mi_tupla = tuple(mi_lista)
print(mi_tupla)  # Salida: (2, 4, 6)
print(type(mi_tupla))  # Salida: <class 'tuple'>

# De la misma manera, cuando se desea convertir un iterable en una liste, se puede emplear
# la función integrada de Python denominada list():
mi_tupla = 1, 2, 3,
mi_lista = list(mi_tupla)
print(type(mi_lista))  # outputs: <class 'list'>
