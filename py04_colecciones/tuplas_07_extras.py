# EXTRA
# También se puede crear una tupla utilizando la función integrada de Python tuple().
# Esto es particularmente útil cuando se desea convertir un iterable en una tupla
# (por ejemplo, una lista, rango, cadena, etcétera):
miTup = tuple((1, 2, "cadena"))
print(miTup)  # salida: (1, 2, 'cadena')
print(type(miTup))  # salida: <class 'tuple'>
print()

# podemos convertir una lista en tupla
lst = [2, 4, 6]
print(lst)  # salida: [2, 4, 6]
print(type(lst))  # salida: <class 'list'>

tup = tuple(lst)
print(tup)  # salida: (2, 4, 6)
print(type(tup))  # salida: <class 'tuple'>

# De la misma manera, cuando se desea convertir un iterable en una liste, se puede emplear
# la función integrada de Python denominada list():
print('\nejemplo de tupla a lista')
tup = 1, 2, 3,
lst = list(tup)
print(lst)
print(type(lst))  # salida: <class 'list'>
