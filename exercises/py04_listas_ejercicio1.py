# ¿Cuál es la salida del siguiente fragmento de código?
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
other_list = []
agregar = 0

for number in my_list:
    agregar = 2 ** number  # Equivale a agregar = agregar * number
    other_list.append(agregar)

print(other_list)
