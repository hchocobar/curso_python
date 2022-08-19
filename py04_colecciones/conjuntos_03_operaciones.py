# Operaciones con conjuntos
# Debes notar que la salida no siempre se muestran en el mismo orden si ejecutas varias veces el programa
a = set('abracadabra')
b = set('alacazam')

# letras únicas en a
print(a)  # salida: {'r', 'b', 'd', 'c', 'a'}
print(b)  # salida: {'l', 'a', 'c', 'm', 'z'}

# letras únicas en a pero no en b
print(a - b)  # salida: {'r', 'd', 'b'}

# letras en a o b o en ambas
print(a | b)  # salida {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

# letras en a y b
print(a & b)  # salida: {'a', 'c'}

# letras en a o b pero no en ambas
print(a ^ b)  # salida: {'r', 'd', 'b', 'm', 'z', 'l'}
