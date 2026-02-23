# Podemos utilizar una lista como argumento / parámetro de una función
def hola_a_todos(my_list):
    for nombre in my_list:
        print("Hola,", nombre)


# hola_a_todos(["Juan", "Lucía", "Gustavo", "Sofía", "Roberto", "Héctor"])
lista_nombres = ["Juan", "Lucía", "Gustavo", "Sofía", "Roberto", "Héctor"]
# hola_a_todos(lista_nombres)


# Podemos obtener una lista como resultado de función
def creando_listas(last_number):
    """
    Crea una lista desde uno hasta el valor recibido

    :param last_number: debe ser un entero mayor que uno (1)
    :return: los dobles de los enteros
    """
    my_list = []
    for number in range(1, last_number + 1):
        my_list.append(f'el doble de {number} es {number * 2}')
    return my_list


print(creando_listas(5))  # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
