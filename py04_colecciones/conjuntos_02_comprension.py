# Construcción de un conjunto utilizando comprensión
set_a = {x for x in 'abracadabra'}  # Valores de x en cada iteración: a, b, r, a, c, d, a, b, r, a
print(set_a)  # Salida {'r', 'c', 'a', 'b', 'd'}

# Otro ejemplo
set_a = {x for x in 'abracadabra' if x not in 'abc'}
print(set_a)  # Salida {'r', 'd'}
