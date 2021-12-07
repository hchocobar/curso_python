# Cuando se le asigna a una variable (o se devuelve como el resultado de una función).
# Cuando se compara con una variable para diagnosticar su estado interno.
# si una función no devuelve un cierto valor utilizando una cláusula de expresión return,
# se asume que devuelve implícitamente None.
valor = None
if valor is None:
    print("Lo siento, no tienes ningún valor\n")


def my_function(a, b):
    return


print(my_function(3, 4))  # salida: None


# Observemos este otro ejemplo:
def strange_function(n):
    if n % 2 == 0:
        return "número par"
    # else:  ## si no agregamos este bloque, en caso de n impar, la función retorna None
    #    return "numero impar"


print(strange_function(18))  # Salida: True
print(strange_function(45))  # Salida: None
