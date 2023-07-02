# Podemos emplear el bucle for para iterar a través del diccionario
mi_diccionario = {'nombre': 'Jane Doe',
                  'edad': 23,
                  'curso': 'Curso de Python',
                  'skills': {'programación': True,
                             'base_de_datos': False},
                  'niveles': ['básico', 'intermedio']}

for item in mi_diccionario:
    print(item)

# Salida:
"""
nombre
edad
curso
skills
niveles
"""
