# Colecciones

<!-- TOC -->
* [Colecciones](#colecciones)
  * [Listas](#listas)
    * [Definición](#definición)
    * [Puntos claves](#puntos-claves)
    * [Métodos](#métodos)
<!-- TOC -->

## Listas

### Definición

Una lista en Python es una colección ordenada y mutable de elementos separados por comas entre corchetes.

### Puntos claves

1. La lista es un tipo de dato en Python que se utiliza para almacenar múltiples objetos.
```python
# Ejemplo de lista en Python
mi_lista = [1, None, True, "Soy una cadena", 256, 0]
```

2. Las listas se pueden indexar.
```python
mi_lista = [1, None, True, 'Soy una cadena', 256, 0]
print(mi_lista[3])  # Salida: Soy una cadena
print(mi_lista[-1])  # Salida: 0

mi_lista[1] = '?'
print(mi_lista)  # Salida: [1, '?', True, 'Soy una cadena', 256, 0]
```

3. Las listas pueden estar anidadas.
```python
mi_lista = [1, 'a', ["lista", 64, [0, 1], False]]
```

4. Los elementos de la lista y las listas se pueden eliminar.
```python
mi_lista = [1, 2, 3, 4]
del mi_lista[2]
print(mi_lista)  # Salida: [1, 2, 4]

del mi_lista  # Elimina toda la lista 
```

5. Las listas pueden ser iteradas mediante el uso del bucle `for`.
```python
mi_lista = ["blanco", "purpura", "azul", "amarillo", "verde"]

for color in mi_lista:
    print(color) 
```

6. La función `len()` es utilizada para verificar la longitud de la lista.
```python
mi_lista = ["blanco", "purpura", "azul", "amarillo", "verde"]
print(len(mi_lista))  # Salida: 5
```

### Métodos

1. Las listas se pueden actualizar, utilizando los métodos `insert()` y `append()` respectivamente.
```python

mi_lista = [1, None, True, 'Soy una cadena', 256, 0]
mi_lista.insert(0, "first")
mi_lista.append("last")

print(mi_lista)  # Salida: ['first', 1, None, True, 'Soy una cadena', 256, 0, 'last'] 
```

2. Podemos usar el método `sort()` para ordenar los elementos de una lista.
```python
mi_lista = [5, 3, 1, 2, 4]
mi_lista.sort()

print(mi_lista)  # Salida: [1, 2, 3, 4, 5]
```

2. Podemos utilizar el método `reverse()` para invertir la lista.
```python
mi_lista = [5, 3, 1, 2, 4]
mi_lista.reverse()

print (mi_lista)  # Salida: [4, 2, 1, 3, 5]
```

3. Más métodos de las listas: `remove()`, `pop()`, `clear()`, `count()`, `copy()`, y más en la 
[documentación oficial de Python](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

