# Listas - 01 - Introducción
# Asignación de una lista a una variable
# Sintaxis: my_list = [elem1, elem2, elem3]
numbers = [4, 5, 6, 22, "h"]
print(numbers)  # Imprimiendo el contenido de la lista original
print(type(numbers))


# Asignación de un valor a un elemento
print(numbers[0])
numbers[0] = 101  # Asignación de un valor a un elemento en una lista
print(numbers)  # Imprimiendo contenido de la lista con cambio en el valor del primer elemento
numbers[1] = numbers[3]  # Copiando el valor del quinto elemento al segundo elemento
print(numbers)  # Imprimiendo contenido de la lista con los cambios
print('longitud de la lista:', len(numbers))  # Imprimiendo la longitud de la lista


# Índices negativos
# Los índices negativos son válidos
print(numbers)  # Imprimiendo el contenido de la lista actual
print('con len ----:', numbers[len(numbers)-1])
print('con negativo:', numbers[-1])  # -1 -> último elemento en la lista
print(numbers[-2])  # -2 -> penúltimo elemento en la lista


# Eliminar un elemento de la lista
del numbers[1]  # Eliminando el segundo elemento de la lista
print(numbers)  # Imprimiendo el contenido de la lista actual
print(len(numbers))  # Imprimiendo nueva longitud de la lista


# Agregar un elemento al final de la lista
# Método append() para listas
lista2 = [5, 35, 76, 220, "hector"]
numbers.append("a")  # Agrega un elemento al final de la lista y le asigna el valor "a"
print(numbers)
print(len(numbers))
lista2.reverse()
lista2.append("Federico")
print(lista2)


# Insertar un elemento en cualquier lugar de la lista
# Método insert() para listas
numbers.insert(1, 222)  # Inserta un elemento en el segundo lugar y le asigna el valor 222
print(numbers)
print(len(numbers))


# Review
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

