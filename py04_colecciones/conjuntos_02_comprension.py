# Construcción de un conjunto utilizando comprensión
a = {x for x in 'abracadabra'}  # a, b, r, a, c, d, a, b, r, a
print(a)  # salida {'r', 'c', 'a', 'b', 'd'}

# otro ejemplo
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)  # salida {'r', 'd'}
