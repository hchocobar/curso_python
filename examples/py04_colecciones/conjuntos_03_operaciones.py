# Operaciones con conjuntos
# Notarás que la salida no siempre se muestran en el mismo orden si ejecutas varias veces el programa
set_a = set('abracadabra')
set_b = set('alacazam')

# Letras únicas en los conjuntos
print(set_a)  # Salida: {'r', 'b', 'd', 'c', 'a'}
print(set_b)  # Salida: {'l', 'a', 'c', 'm', 'z'}

# Letras únicas en set_a pero no en set_b
print(set_a - set_b)  # Salida: {'r', 'd', 'b'}

# letras en set_a o set_b o en ambas
print(set_a | set_b)  # Salida {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

# letras en set_a y set_b
print(set_a & set_b)  # Salida: {'a', 'c'}

# letras en set_a o set_b pero no en ambas
print(set_a ^ set_b)  # Salida: {'r', 'd', 'b', 'm', 'z', 'l'}
