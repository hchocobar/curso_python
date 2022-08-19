# Listas - 01 - Introducción
# Asignación de una lista a una variable
# Sintaxis: my_list = [elem1, elem2, elem3]
# Asignación de un valor a un elemento
# Indices negativos
# Eliminar un elemento de la lista
# Agregar un elemento al final de la lista
# Insertar un elemento en cualquier lugar de la lista
numbers = [4, 5, 6, 22, "h"]
print(numbers)  # imprimiendo el contenido de la lista original
print(type(numbers))
# # print(numbers[0])
# numbers[0] = 101  # Asignación de un valor a un elemento en una lista
# print(numbers)  # imprimiendo contenido de la lista con cambio en el valor del primer elemento
#
# numbers[1] = numbers[3]  # copiando el valor del quinto elemento al segundo elemento
# # print(numbers)  # imprimiendo contenido de la lista con los cambios
# # print('longitud de la lista', len(numbers))  # imprimiendo la longitud de la lista
#
# # Los índices negativos son válidos
# print(numbers)  # imprimiendo el contenido de la lista actual
# # print('con len ----:', numbers[len(numbers)-1])
# # print('con negativo:', numbers[-1])  # -1 -> último elemento en la lista
# # print(numbers[-2])  # -2 -> anteúltimo elemento en la lista


# del numbers[1]  # eliminando el segundo elemento de la lista
# print(numbers)  # imprimiendo el contenido de la lista actual
# print(len(numbers))  # imprimiendo nueva longitud de la lista


# método append para listas
lista2 = [5, 35, 76, 220, "hector"]
numbers.append("a")  # Agrega un elemento al final de la lista y le asigna el valor "a"
print(numbers)
print(len(numbers))
lista2.reverse()
lista2.append("Federico")
print(lista2)

# método insert para listas
numbers.insert(1, 222)  # Inserta un elemento en el 2do lugar y le asigna el valor 222
print(numbers)
print(len(numbers))
dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']
dias[0] = 'monday'
dias.append('sábado')
dias.append('domingo')
dias.insert(2, 'otro dia')
print(dias)
print(len(dias))
print(dias[6], dias[0])
print(type(dias))
dias_semana = dias.copy()
print(dias_semana)
print(numbers.count(6))

