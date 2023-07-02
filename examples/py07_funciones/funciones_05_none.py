# Si una función no devuelve un valor con la cláusula return, se asume que devuelve implícitamente None.
def my_function(a, b):
    return


# Observemos este otro ejemplo:
def strange_function(n):
    if n % 2 == 0:
        return "número par"
    # else:  # si no agregamos este bloque, en caso de n impar, la función retorna None
    #     return "número impar"


print(my_function(3, 4))  # Salida: None
print(strange_function(18))  # Salida: "número par"
print(strange_function(45))  # Salida: None

# Además, podemos utilizar None cuando:
# Lo asignamos a una variable (o se devuelve como el resultado de una función).
# La utilizamos para comparar una variable para diagnosticar su estado interno.
valor = None
if valor is None:
    print("Lo siento, no tienes ningún valor\n")
