# Argumentos Listas:
# Si el argumento es una lista, el cambiar el valor del parámetro correspondiente no afecta la lista
# (Recuerda: las variables que contienen listas son almacenadas de manera diferente que las escalares).
def my_function_list(my_list_1):
    print(my_list_1)  # Salida: [2, 3, 4]
    my_list_1 = my_list_1[0] * 5  # La variable my_list_1 deja de contener una lista y pasa a contener un entero
    print(my_list_1)  # Salida: 10
    my_list_1 = "Hola"
    print(my_list_1)  # Salida: Hola


my_list_2 = [2, 3, 4]
my_function_list(my_list_2)
print('el valor de my_list_2 es:', my_list_2)  # Salida: el valor de my_list_2 es: [2, 3, 4]

print("\nVeamos otro ejemplo:")


# Pero si se modifica la lista identificada por el parámetro, la lista reflejará el cambio.
# Nota: ¡La lista no el parámetro!
def my_function(mi_list_3):
    print(mi_list_3)
    del mi_list_3[0]  # Eliminamos el elemento 0 de la lista


mi_list_4 = [6, 7, 8]
my_function(mi_list_4)  # Salida: [6, 7, 8]
print(mi_list_4)  # Salida [7, 8]

# Recordemos:
# La asignación de una lista no realiza una copia del contenido de la lista, sino que hace que ambas variables apunten
# a la misma lista en la memoria.
# Entonces, si deseamos hacer una copia del contenido de la lista debemos utilizar 'Rodajas'
