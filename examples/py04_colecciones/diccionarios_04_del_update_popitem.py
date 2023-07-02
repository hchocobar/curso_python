# Para agregar o eliminar una clave (junto con su valor asociado), emplea la siguiente sintaxis:
mi_directorio = {}  # Un diccionario vacío
print(mi_directorio)

mi_directorio["Adan"] = 345678395  # Crea o añade un par clave-valor
mi_directorio["Eva"] = 345234567  # Crea o añade un par clave-valor
print(mi_directorio)  # Salida: {'Adan': 3456783958, 'Eva': 345234567}

del mi_directorio["Adan"]
print(mi_directorio)  # Salida: {'Eva': 345234567}

# Además, se puede insertar un elemento a un diccionario utilizando el método update(),
mi_diccionario1 = {"flower": "flor"}
print(mi_diccionario1)
mi_diccionario2 = {"earth": "tierra"}
print(mi_diccionario2)

mi_diccionario1.update(mi_diccionario2)
print(mi_diccionario1)  # Salida: {'flower' : 'flor', 'earth' : 'tierra'}
mi_diccionario2.update(mi_diccionario1)
print(mi_diccionario2)

# Eliminamos el último elemento con el método popitem(), por ejemplo:
print()
mi_diccionario1.popitem()
print(mi_diccionario1)  # Salida: {'flower' : 'flor'}
