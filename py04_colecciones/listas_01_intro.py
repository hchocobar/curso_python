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

numbers[0] = 101  # Asignación de un valor a un elemento en una lista
print(numbers)  # imprimiendo contenido de la lista con cambio en el valor del primer elemento

numbers[1] = numbers[3]  # copiando el valor del quinto elemento al segundo elemento
print(numbers)  # imprimiendo contenido de la lista con los cambios
print(len(numbers))  # imprimiendo la longitud de la lista

# Los índices negativos son válidos
print(numbers)  # imprimiendo el contenido de la lista actual
print(numbers[-1])  # -1 -> último elemento en la lista
print(numbers[-2])  # -2 -> anteúltimo elemento en la lista


del numbers[1]  # eliminando el segundo elemento de la lista
print(numbers)  # imprimiendo el contenido de la lista actual
print(len(numbers))  # imprimiendo nueva longitud de la lista


# método append para listas
numbers.append("a")  # Agrega un elemento al final de la lista y le asigna el valor "a"
print(numbers)
print(len(numbers))

# método insert para listas
numbers.insert(1, 222)  # Inserta un elemento en el 2do lugar y le asigna el valor 222
print(numbers)
print(len(numbers))
