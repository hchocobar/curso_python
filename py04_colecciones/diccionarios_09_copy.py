# Para copiar un diccionario, emplea el método copy():
mi_diccionario = {'nombre': 'Jane Doe',
                  'edad': 23,
                  'curso': 'Curso de Python',
                  'skills': {'programación': True,
                             'base_de_datos': False},
                  'niveles': ['básico', 'intermedio']}

copia_mi_diccionario = mi_diccionario.copy()
print(copia_mi_diccionario)
print(type(copia_mi_diccionario))
