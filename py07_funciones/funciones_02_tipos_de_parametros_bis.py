# Argumentos posicionales: importa el orden de los parámetros
# Argumentos con palabras clave: el orden de los argumentos es irrelevante
# Mix de Argumentos posicionales con palabras clave: siempre los posicionales primero
def my_function(a, b=0, c=1):
    print(a - int(b) / c)


my_function(5, "2")  # salida: 3
my_function(2, 5, 3)  # salida: -6


my_function(a=5, b=2, c=4)  # salida: 3
my_function(b=5, c=2, a=4)  # salida: 3


my_function(5, b=2)  # salida: 3
my_function(5, c=2)  # salida: 3

