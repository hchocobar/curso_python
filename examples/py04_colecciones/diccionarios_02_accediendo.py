# Si deseamos acceder a un elemento del diccionario, tenemos dos formas de hacerlo
mi_diccionario = {'nombre': 'Jane Doe',
                  'edad': 23,
                  'curso': 'Curso de Python',
                  'skills': {'programación': True,
                             'base_de_datos': False},
                  'niveles': ['básico', 'intermedio']}

# 1. Referencia a su clave colocándola dentro de corchetes []
print(mi_diccionario["nombre"])  # Salida: 'Jane Doe'

# 2. Utilizando el método get()
result = mi_diccionario.get("fecha", 'La fecha de hoy')

print(result)  # Salida: 'Curso de Python'
