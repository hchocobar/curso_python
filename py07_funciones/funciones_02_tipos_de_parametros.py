# Argumentos posicionales: importa el orden de los parámetros
# Argumentos con palabras clave: el orden de los argumentos es irrelevante
# Mix de Argumentos posicionales con palabras clave: siempre los posicionales primero
def my_function(a, b, c=1):
    print(a - b / c)


my_function(5, 2)  # salida: 3
my_function(2, 5, 3)  # salida: -6


my_function(a=5, b=2, c=4)  # salida: 3
my_function(a=5, b=2, c=4)  # salida: 3


my_function(5, b=2, c=4)  # salida: 3
my_function(5, b=2, c=7)  # salida: 3

