# Las listas (y muchas otras entidades complejas de Python) se almacenan de diferentes maneras
# que las variables ordinarias (escalares).
#
# Se podría decir que:
# # * El nombre de una variable ordinaria es el nombre de su contenido.
# * El nombre de una lista es el nombre de una ubicación de memoria donde se almacena la lista.
#
# En el ejemplo que sigue La asignación: lista2 = lista1 copia el nombre de la matriz, no su contenido.
# En efecto, los dos nombres (lista1 y lista2) identifican la misma ubicación en la memoria de la computadora.
# Modificar uno de ellos afecta al otro, y viceversa.
lista1 = [1]
lista2 = lista1
lista1[0] = 2
print(lista2)

# Copiando toda la lista mediante una rodaja (slicing)
lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)

# Copiando parte de la lista mediante una rodaja (slicing)
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:3]
print(nuevaLista)

# Utilizando inicio o fin negativos...
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:-1]
print(nuevaLista)

# operadores in y not
miLista = [0, 3, 12, 8, 2]
print(5 in miLista)
print(5 not in miLista)
print(12 in miLista)
