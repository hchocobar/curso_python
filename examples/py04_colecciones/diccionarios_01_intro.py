""" Los diccionarios son colecciones indexadas de datos, mutables y desordenadas.
A partir de Python 3.6x los diccionarios están ordenados de manera predeterminada.
Cada diccionario es un par de clave: valor. """

# Podemos crear un diccionario empleando la siguiente sintaxis:
mi_diccionario = {'nombre': 'Jane Doe',
                  'edad': 23,
                  'curso': 'Curso de Python',
                  'skills': {'programación': True,
                             'base_de_datos': False},
                  'niveles': ['básico', 'intermedio']}

print(mi_diccionario)
print(type(mi_diccionario))
