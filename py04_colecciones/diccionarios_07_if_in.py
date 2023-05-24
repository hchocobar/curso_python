# Para comprobar si una clave existe en un diccionario, se puede emplear la palabra reservada in:
mi_diccionario = {'nombre': 'Jane Doe',
                  'edad': 23,
                  'curso': 'Curso de Python',
                  'skills': {'programación': True,
                             'base_de_datos': False},
                  'niveles': ['básico', 'intermedio']}

# Prueba si "nombre" está en mi_diccionario
if "nombre" in mi_diccionario:
    print("SI")
else:
    print("NO")
