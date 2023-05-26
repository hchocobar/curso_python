# EXTRA
# También se puede crear una tupla utilizando la función integrada de Python tuple()
# Esto es particularmente útil cuando se desea convertir un iterable en una tupla
# (por ejemplo, una lista, rango, cadena, etcétera):
mi_tupla = tuple((1, 2, "cadena"))
print(mi_tupla)  # Salida: (1, 2, 'cadena')
print(type(mi_tupla))  # Salida: <class 'tuple'>
print()

# podemos convertir una lista en tupla
mi_lista = [2, 4, 6]
print(mi_lista)  # Salida: [2, 4, 6]
print(type(mi_lista))  # Salida: <class 'list'>

mi_tupla = tuple(mi_lista)
print(mi_tupla)  # Salida: (2, 4, 6)
print(type(mi_tupla))  # Salida: <class 'tuple'>

# De la misma manera, cuando se desea convertir un iterable en una liste, se puede emplear
# la función integrada de Python denominada list():
print('\nEjemplo de tupla a lista')
mi_tupla = 1, 2, 3,
mi_lista = list(mi_tupla)
print(mi_lista)  # Salida: [1, 2, 3]
print(type(mi_lista))  # Salida: <class 'list'>
