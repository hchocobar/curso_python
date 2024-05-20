"""
Condicionales:
 - Estructura if-elif-else
 - Operadores lógicos: and  or  not

Loops:
 - while
 - for in 
  - iterables
  - range(start, stop, step)
 - break, continue

Indentación y bloques
  - pass
"""

# Hola Mundo
name = 'Hector'  # Variable string
message = 'Bienvenido!'  # Variable string
# print('Hola', name, message)
condition = False

if name or condition:
    print('imprime linea 24, True')
else:
    print('imprime linea 26, False')

# for item in message:
#     print(item)

# for item in range(1, 11):  # 1, 3, 5, 7, 9
#     if item % 2 == 0:
#         print(item)
#         continue
#         print('no se imprime')
# print('fin')

# break - salta / sale del ciclo inmediatamente
# continue - Vuelve al inicio del ciclo sin ejecutar las lineas posteriores
