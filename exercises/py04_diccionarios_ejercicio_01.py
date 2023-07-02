# Escribe un programa que "una" los dos diccionarios (d1 y d2) para crear uno nuevo (d3).
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
for elemento in (d1, d2):
    pass  # El comando pass no realiza nada, pero es necesario en el ejemplo xq el bloque debe tener algo
    # Elimina el comando pass y agrega tu código aquí
print(d3)

# Solución Muestra:
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
for elemento in (d1, d2):
    d3.update(elemento)
print(d3)
print(type(d3))
