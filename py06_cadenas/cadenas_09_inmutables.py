# las cadenas de Python son secuencias inmutables
alfabeto = "abcdefghijklmnopqrstuvwxyz"

# del - no podemos borrar un elemento de la lista, pero si podemos borrarla completa
# del alfabeto[0]  # TypeError: 'str' object doesn't support item deletion
del alfabeto

alfabeto = "abcdefghijklmnopqrstuvwxyz"
# los métodos append() e insert() no están disponibles en cadenas
# alfabeto.append("A")  # AttributeError: 'str' object has no attribute 'append'
# alfabeto.insert(0, "A")  # AttributeError: 'str' object has no attribute 'insert'

# list() - convierte una cadena en una lista
print(alfabeto)
print(list(alfabeto))
