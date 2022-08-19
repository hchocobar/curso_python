# Para agregar o eliminar una clave (junto con su valor asociado), emplea la siguiente sintaxis:
miDirectorio = {}  # un diccionario vacío
print(miDirectorio)

miDirectorio["Adan"] = 345678395  # crea o añade un par clave-valor
print(miDirectorio)  # salida: {'Adan': 3456783958}
miDirectorio["Eva"] = 345234567  # crea o añade un par clave-valor
print(miDirectorio)  # salida: {'Adan': 3456783958, 'Eva': 345234567}

del miDirectorio["Adan"]
print(miDirectorio)  # salida: {'Eva': 345234567}

# Además, se puede insertar un elemento a un diccionario utilizando el método update(),
miDiccionario1 = {"flower": "flor"}
print(miDiccionario1)
miDiccionario2 = {"earth": "tierra"}
print(miDiccionario2)

miDiccionario1.update(miDiccionario2)
print(miDiccionario1)  # salida: {'flower' : 'flor', 'earth' : 'tierra'}
miDiccionario2.update(miDiccionario1)
print(miDiccionario2)

# y eliminar el último elemento con el método popitem(), por ejemplo:
print()
miDiccionario1.popitem()
print(miDiccionario1)  # salida: {'flower' : 'flor'}
