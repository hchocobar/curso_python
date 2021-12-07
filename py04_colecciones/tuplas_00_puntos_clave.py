# 1. Las Tuplas son colecciones de datos ordenadas e inmutables.
# Se puede pensar en ellas como listas inmutables.
# Se definen con paréntesis:
miTupla = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
print(miTupla)

miLista = [1, 2, True, "una cadena", (3, 4), [5, 6], None]
print(miLista)

# Cada elemento de la tupla puede ser de un tipo de dato diferente (por ejemplo, enteros, cadenas, boleanos, etc.).
# Las tuplas pueden contener otras tuplas o listas (y viceversa).

# 2. Se puede crear una tupla vacía de la siguiente manera:
tuplaVacia = ()
print(type(tuplaVacia))  # salida: <class 'tuple'>

# 3. La tupla de un solo elemento se define de la siguiente manera:
tuplaUnElemento = ("uno",)  # paréntesis y coma
tuplaUnElemento2 = "uno",  # sin paréntesis, solo la coma

# Si se elimina la coma, Python creará una variable no una tupla:
miTup1 = 1,
print(type(miTup1))  # salida: <class 'tuple'>
miTup2 = 1
print(type(miTup2))  # salida: <class 'int'>

# 4. Se pueden acceder los elementos de la tupla al indexarlos:
miTupla = (1, 2.0, "cadena", [3, 4], (5,), True)
print(miTupla[3])  # salida: [3, 4]

# 5. Las tuplas son inmutables, lo que significa que no se puede agregar, modificar, cambiar o quitar elementos.
# El siguiente fragmento de código # provocará una excepción:
miTupla = (1, 2.0, "cadena", [3, 4], (5,), True)
miTupla[2] = "guitarra"  # se levanta una excepción TypeError

# Sin embargo, se puede eliminar la tupla completa:
miTupla = 1, 2, 3,
del miTupla
print(miTupla)  # NameError: name 'miTupla' is not defined

# 6. Puedes navegar a través de los elementos de una tupla con un bucle
# Ejemplo 1 - verificar si un elemento o no esta presente en la tupla
t1 = (1, 2, 3)
for elem in t1:
    print(elem)

# Ejemplo 2 - emplear la función len() para verificar cuantos elementos existen en la tupla
t2 = (1, 2, 3, 4)
print(5 in t2)
print(5 not in t2)

# Ejemplo 3 -  incluso unir o multiplicar tuplas
t3 = (1, 2, 3, 5)
print(len(t3))

# Ejemplo 4
t4 = t1 + t2
t5 = t3 * 2
print(t4)
print(t5)

# EXTRA
# También se puede crear una tupla utilizando la función integrada de Python tuple().
# Esto es particularmente útil cuando se desea convertir un iterable en una tupla
# (por ejemplo, una lista, rango, cadena, etcétera):
miTup = tuple((1, 2, "cadena"))
print(miTup)
lst = [2, 4, 6]
print(lst)  # salida: [2, 4, 6]
print(type(lst))  # salida: <class 'list'>
tup = tuple(lst)
print(tup)  # outputs: (2, 4, 6)
print(type(tup))  # salida: <class 'tuple'>

# De la misma manera, cuando se desea convertir un iterable en una liste, se puede emplear
# la función integrada de Python denominada list():
tup = 1, 2, 3,
lst = list(tup)
print(type(lst))  # outputs: <class 'list'>
