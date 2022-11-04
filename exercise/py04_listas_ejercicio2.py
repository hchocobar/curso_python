# ¿Cuál es la salida del siguiente fragmento de código?
lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = []
agregar = 0

for number in lst:
    agregar = 2 ** number  # agregar = agregar * number
    lst2.append(agregar)

print(lst2)
