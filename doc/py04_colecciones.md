# Colecciones

<!-- TOC -->
* [Colecciones](#colecciones)
  * [Listas](#listas)
    * [Definición](#definición)
    * [Puntos claves](#puntos-claves)
    * [Métodos](#métodos)
  * [Tuplas](#tuplas)
    * [Definición](#definición-1)
    * [Puntos claves](#puntos-claves-1)
    * [Función `tuple()`](#función-tuple)
  * [Diccionarios](#diccionarios)
    * [Definición](#definición-2)
    * [Puntos Claves](#puntos-claves-2)
  * [Conjuntos](#conjuntos)
  * [Casos especiales](#casos-especiales)
    * [Colas](#colas)
    * [Pilas](#pilas)
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

## Tuplas

### Definición

Las Tuplas son colecciones de datos ordenadas e inmutables.

### Puntos claves

1. Se puede pensar en ellas como listas inmutables. Se definen con paréntesis. Cada elemento de la tupla puede ser de un tipo de dato diferente (por ejemplo, enteros, cadenas, boleanos, etc.). Las tuplas pueden contener otras tuplas o listas (y viceversa).

```python
mi_tupla = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
print(mi_tupla)

mi_lista = [1, 2, True, "una cadena", (3, 4), [5, 6], None]
print(mi_lista)
```

2. Se puede crear una tupla vacía de la siguiente manera:

```python
mi_tupla = ()
print(type(mi_tupla))  # Salida: <class 'tuple'>
```

3. La tupla de un solo elemento se define de la siguiente manera:

```python
tupla_un_elemento_1 = ("uno", )  # Paréntesis y coma
tupla_un_elemento_2 = "uno",  # Sin paréntesis, solo la coma
mi_tupla = 1, 
print(type(mi_tupla))  # Salida: <class 'tuple'>

# Si se elimina la coma, Python creará una variable literal, no una tupla:
number = 1
print(type(number))  # Salida: <class 'int'>
```

4. Se pueden acceder los elementos de la tupla al indexarlos:

```python
mi_tupla = (1, 2.0, "cadena", [3, 4], (5, ), True)
print(mi_tupla[3])  # Salida: [3, 4]
print(mi_tupla[2])  # Salida: "cadena"
```

5. Las tuplas son inmutables, lo que significa que no se puede agregar, modificar, cambiar o quitar elementos. El siguiente fragmento de código provocará una excepción:

```python
mi_tupla = (1, 2.0, "cadena", [3, 4], (5, ), True)
mi_tupla[2] = "guitarra"  # Se levanta una excepción TypeError
```

6. Podemos eliminar una tupla completa:

```python
mi_tupla = 1, 2, 3,  # Sin paréntesis
del mi_tupla
print(mi_tupla)  # NameError: name 'mi_tupla' is not defined
```

7. Puedes navegar a través de los elementos de una tupla con un bucle (Ejemplo 1), verificar si un elemento o no está presente en la tupla (Ejemplo 2), emplear la función `len()` para verificar cuantos elementos existen en la tupla (Ejemplo 3), o incluso unir o multiplicar tuplas (Ejemplo 4):

```python
# Ejemplo 1
tupla_1 = (1, 2, 3)
for item in tupla_1:
    print(item)

# Ejemplo 2
tupla_2 = (1, 2, 3, 4)
print(5 in tupla_2)  # Salida: False
print(5 not in tupla_2)  # Salida: True

# Ejemplo 3
tupla_3 = (1, 2, 3, 5)
print(len(tupla_3))  # Salida: 4

# Ejemplo 4
tupla_4 = tupla_1 + tupla_2
tupla_5 = tupla_3 * 2
print(tupla_4)  # Salida: (1, 2, 3, 1, 2, 3, 4)
print(tupla_5)  # Salida: (1, 2, 3, 5, 1, 2, 3, 5)
```

### Función `tuple()`

También podemos crear una tupla utilizando la función integrada de Python `tuple()`. Esto es particularmente útil cuando se desea convertir un iterable (por ejemplo, una lista, rango, cadena, etcétera) en una tupla.

```python
mi_tupla = tuple((1, 2, "cadena"))
print(mi_tupla)  # Salida: (1, 2, 'cadena')

mi_lista = [2, 4, 6]
print(mi_lista)  # Salida: [2, 4, 6]
print(type(mi_lista))  # Salida: <class 'list'>

mi_tupla = tuple(mi_lista)
print(mi_tupla)  # Salida: (2, 4, 6)
print(type(mi_tupla))  # Salida: <class 'tuple'>
```

De la misma manera, cuando se desea convertir un iterable en una lista, se puede emplear la función integrada de Python denominada `list()`.

```python
mi_tupla = 1, 2, 3, 
mi_lista = list(mi_tupla)
print(type(mi_lista))  # Salida: <class 'list'>
```

## Diccionarios

### Definición

Los diccionarios son colecciones indexadas de datos, mutables y desordenadas.

> Nota: Desde Python 3.6x los diccionarios están ordenados de manera predeterminada.

### Puntos Claves

1. Cada diccionario es un par de `clave : valor`. Podemos crearlo empleado la siguiente sintaxis:

```python
mi_diccionario = {clave_1 : valor_1,
                  clave_3 : valor_3,
                  clave_2 : valor_2}

```

2. Si se desea acceder a un elemento del diccionario, se puede hacer haciendo referencia a su clave colocándola dentro de corchetes (ejemplo 1) o utilizando el método get() (ejemplo 2):

```python
person = {"first_name": 'Joe',
          "last_name": "Doe",
          "email": "joe.doe@domain.com"}

element = person["email"]  # Ejemplo 1
print(element)  # Salida: joe.doe@domain.com

item = person.get("last_name")  # Ejemplo 2
print(item)  # Salida: Doe
```

3. Cambiamos el valor asociado a una clave específica, haciendo referencia a la clave del elemento.

```python
person = {"first_name": "unknown",
          "last_name": "Doe",
          "email": "unknown"}

person["first_name"] = "Joe"  
person['email'] = "joe.doe@domain.com"
print(person)  # Salida: {'first_name': 'Joe', 'last_name': 'Doe', 'email': 'joe.doe@domain.com'}
```

4. Para agregar o eliminar una clave (junto con su valor asociado), utilice la siguiente sintaxis:

```python
mi_agenda = {}  # Crea un diccionario vacio

mi_agenda["Adan"] = 3323314748  # Crea o añade un par clave-valor
mi_agenda["Jane"] = 3015005042  # Crea o añade un par clave-valor

print(mi_agenda)  # Salida: {'Adan': 3323314748, 'Jane': 3015005042}

del mi_agenda["Adan"]
print(mi_agenda)  # Salida: {'Jane': 3015005042}
```

5. Además, se puede insertar un elemento a un diccionario utilizando el método `update()`, y eliminar el ultimo elemento con el método `popitem()`, por ejemplo:

```python
person = {"first_name": 'Joe',
          "last_name": "Doe",
          "email": "joe.doe@domain.com"}

person.update({"age": 35})
print(person)  # Salida: {'first_name': 'Joe', 'last_name': 'Doe', 'email': 'joe.doe@domain.com', 'age': 35}

person.popitem()
print(person)  # Salida: {'first_name': 'Joe', 'last_name': 'Doe', 'email': 'joe.doe@domain.com'}
```

6. Podemos emplear el bucle for para iterar a través del diccionario, por ejemplo:

```python
person = {"first_name": 'Joe',
          "last_name": "Doe",
          "email": "joe.doe@domain.com"}

for clave in person:
    print(clave)  # Salida: first_name
                  #         last_name
                  #         email
```

7. Si deseas examinar los elementos (claves y valores) del diccionario, puedes emplear el método `items()` por ejemplo:

```python
person = {"first_name": 'Joe',
          "last_name": "Doe",
          "email": "joe.doe@domain.com"}

for clave, valor in person.items():
    print("The value of <", clave, "> is:", valor)

# Salida:
# The value of < first_name > is: Joe
# The value of < last_name > is: Doe
# The value of < email > is: joe.doe@domain.com
```

7. Para comprobar si una clave existe en un diccionario, se puede emplear la palabra reservada `in`:

```python
person = {"first_name": 'Joe',
          "last_name": "Doe",
          "email": "joe.doe@domain.com"}

if "name" in person:
    print("La clave existe")
else:
    print("La clave NO existe")

# Salida: La clave NO existe
```


8. Se puede emplear la palabra reservada `del` para eliminar un elemento, o un diccionario entero. Para eliminar todos los elementos de un diccionario se debe emplear el método `clear()`:

```python
person = {"first_name": 'Joe',
          "last_name": "Doe",
          "email": "joe.doe@domain.com"}

print(len(person))  # Salida: 3
del person["first_name"]  # Elimina un elemento
print(len(person))  # Salida: 2

person.clear()  # Elimina todos los elementos
print(len(person))  # Salida: 0

del person  # Elimina el diccionario
```

9. Para copiar un diccionario, emplea el método `copy()`:

```python
person = {"first_name": 'Joe',
          "last_name": "Doe",
          "email": "joe.doe@domain.com"}

copy_person = person.copy()
```

## Conjuntos

## Casos especiales

### Colas

### Pilas