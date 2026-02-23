# Se puede emplear la palabra reservada "del" para eliminar un elemento, o un diccionario entero.
# Para eliminar todos los elementos de un diccionario se debe emplear el método clear():
mi_diccionario = {'nombre': 'Jane Doe',
                  'edad': 23,
                  'curso': 'Curso de Python',
                  'niveles': ['básico', 'intermedio']}

print(len(mi_diccionario))  # Salida: 4
print(mi_diccionario)  # Salida: {'nombre': 'Jane Doe', 'curso': 'Curso de Python', 'niveles': ['básico', 'intermedio']}

del mi_diccionario["edad"]  # Elimina un elemento
print(len(mi_diccionario))  # Salida: 3
print(mi_diccionario)  # Salida: {'nombre': 'Jane Doe', 'curso': 'Curso de Python', 'niveles': ['básico', 'intermedio']}

mi_diccionario.clear()  # Elimina todos los elementos
print(len(mi_diccionario))  # Salida: 0
print(mi_diccionario)  # Salida: {}
#
del mi_diccionario  # elimina el diccionario
print(mi_diccionario)  # Salida: NameError: name 'mi_diccionario' is not defined
