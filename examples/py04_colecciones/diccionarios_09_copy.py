# Para copiar un diccionario, emplea el método copy():
mi_diccionario = {'nombre': 'Jane Doe',
                  'edad': None,
                  'curso': '',
                  'skills': {'programación': True,
                             'base_de_datos': False},
                  'niveles': ['básico', 'intermedio'],
                  'Año de Nacimiento': 1900,}

copia_mi_diccionario = mi_diccionario.copy()
print(copia_mi_diccionario)
print(type(copia_mi_diccionario))

mi_diccionario["edad"] = 24
print('original', mi_diccionario)

print('copia', copia_mi_diccionario)