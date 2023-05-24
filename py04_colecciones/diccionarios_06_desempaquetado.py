# Si deseas examinar los elementos (claves y valores) del diccionario, puedes emplear el método items()
mi_diccionario = {'nombre': 'Jane Doe',
                  'edad': 23,
                  'curso': 'Curso de Python',
                  'skills': {'programación': True,
                             'base_de_datos': False},
                  'niveles': ['básico', 'intermedio']}

# Los elementos de la mi_diccionario.items() serán "desempaquetados" en las variables variable_01, variable_02
for variable_01, variable_02 in mi_diccionario.items():
    print("Par clave/valor del diccionario ->", variable_01, ":", variable_02)

