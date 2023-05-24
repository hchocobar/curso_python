mi_lista = [1, None, True, 256, 'Soy una cadena', 0]
print(mi_lista[4])  # Salida: Soy una cadena
print(mi_lista[-2])  # Salida: Soy una cadena

mi_lista[1] = '?'
print(mi_lista)  # Salida: [1, '?', True, 256, 'Soy una cadena', 0]

mi_lista.insert(2, '**NEW**')
print(mi_lista)  # Salida: [1, '?', '**NEW**', True, 256, 'Soy una cadena', 0]

mi_lista.append('last')
print(mi_lista)  # Salida: [1, '?', '**NEW**', True, 256, 'Soy una cadena', 0, 'last']

mi_lista = [1, 'a', ["lista", 64, [0, 1], False]]
print(mi_lista)  # Salida: [1, 'a', ['lista', 64, [0, 1], False]]
print(mi_lista[2])  # Salida: ['lista', 64, [0, 1], False]

for x in mi_lista:
    print(x)
