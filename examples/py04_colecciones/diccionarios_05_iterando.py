# Podemos emplear el bucle for para iterar a través del diccionario
mi_diccionario = {'nombre': 'Jane Doe',
                  'edad': 23,
                  'curso': 'Curso de Python',
                  'skills': {'programación': True,
                             'base_de_datos': False},
                  'niveles': ['básico', 'intermedio']}


for columnas, value in mi_diccionario.items():
    if columnas == 'edad':
        print('La edad es:', value, 'años')
    elif columnas == 'skills':
        print('Este pibe es bueno en:', value)
    else:
        print(columnas, value)
    print()

hola = 'texto'
# for clave, valor in mi_diccionario.items():
#     print(valor)

# Salida:
"""
nombre
edad
curso
skills
niveles
"""
