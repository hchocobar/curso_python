# Las listas se almacenan de diferentes maneras que las variables ordinarias (escalares).
# Nota: también ocurre con muchas otras entidades complejas de Python
#
# Se podría decir que:
# * El nombre de una variable ordinaria es el nombre de su contenido.
# * El nombre de una lista es el nombre de una ubicación de memoria donde se almacena la lista.

# En el ejemplo que sigue La asignación: lista2 = lista1 copia el nombre de la matriz, no su contenido.
# En efecto, los dos nombres (lista1 y lista2) identifican la misma ubicación en la memoria de la computadora.
# Modificar uno de ellos afecta al otro, y viceversa.
lista1 = [1]
lista2 = lista1
lista1[0] = 2
print(lista2)  # Salida: [2]

# Copiando toda la lista mediante una rodaja (slicing)
lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)  # Salida: [1]

# Copiando parte de la lista mediante una rodaja (slicing)
mi_lista = [10, 8, 6, 4, 2]
nueva_lista = mi_lista[1:3]
print(nueva_lista)  # Salida: [8, 6]

# Utilizando inicio o fin negativos...
mi_lista = [10, 8, 6, 4, 2]
nueva_lista = mi_lista[1:-1]
print(nueva_lista)  # Salida: [8, 6, 4]

# operadores in y not
mi_lista = [0, 3, 12, 8, 2]
print(5 in mi_lista)  # Salida: False
print(5 not in mi_lista)  # Salida: True
print(12 in mi_lista)  # Salida: True
