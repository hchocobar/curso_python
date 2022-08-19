# Podemos utilizar una lista como argumento / parámetro de una función
def hola_a_todos(my_list):
    for nombre in my_list:
        print("Hola,", nombre)


# hola_a_todos(["Juan", "Lucía", "Gustavo", "Sofía", "Roberto", "Héctor"])
lista_nombres = ["Juan", "Lucía", "Gustavo", "Sofía", "Roberto", "Héctor"]
hola_a_todos(lista_nombres)

# Podemos obtener una lista como resultado de función
def creando_listas(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list


print(creando_listas(22))
