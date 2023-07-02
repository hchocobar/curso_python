# Ejemplo 1: var1 existe en el código incluso dentro de la función
var1 = 2


def my_function_01(x):
    return x * var1


print(my_function_01(7))  # Salida: 14


# Ejemplo 2: var2 existe solamente dentro de la función
def my_function_02(x):
    var2 = 5
    return x * var2


print(my_function_02(7))  # Salida: 35


# Ejemplo 3: var está definida en el código y tiene una sombra dentro de la función
def my_function_03(x):
    var = 7
    print(var)  # Salida: 7
    return x * var


var = 3
print(my_function_03(7))  # Salida: 49
print(var)  # Muestra 3 o 7 ?
