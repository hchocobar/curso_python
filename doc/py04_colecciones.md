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
    * [Definición](#definición-3)
    * [Creación de conjuntos](#creación-de-conjuntos)
    * [Construcción por Comprensión](#construcción-por-comprensión)
    * [Operaciones](#operaciones)
  * [Casos especiales](#casos-especiales)
    * [Colas](#colas)
      * [Recordemos](#recordemos)
      * [Usando listas como colas](#usando-listas-como-colas)
    * [Pilas](#pilas)
      * [Recordemos](#recordemos-1)
      * [Usando listas como pilas](#usando-listas-como-pilas)
      * [Implementando Pilas con Clases](#implementando-pilas-con-clases)
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
mi_agenda = {}  # Crea un diccionario vacío

mi_agenda["Adan"] = 3323314748  # Crea o añade un par clave-valor
mi_agenda["Jane"] = 3015005042  # Crea o añade un par clave-valor

print(mi_agenda)  # Salida: {'Adan': 3323314748, 'Jane': 3015005042}

del mi_agenda["Adan"]
print(mi_agenda)  # Salida: {'Jane': 3015005042}
```

5. Además, se puede insertar un elemento a un diccionario utilizando el método `update()`, y eliminar el último elemento con el método `popitem()`, por ejemplo:

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

### Definición

Un conjunto es una colección no ordenada y sin elementos repetidos. Dicho de otra manera: colección no ordenada de objetos distintos.

### Creación de conjuntos

Las `{}` llaves o la función `set()` se utilizan para crear conjuntos.

**Nota:** Para crear un conjunto vacío se debe utilizar `set()`, no `{}` porque sino estamos creando un diccionario vacío.

Una pequeña demostración:

```python
# Creación de conjunto mediante {}

mi_conjunto = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(mi_conjunto)  # Salida: {'orange', 'banana', 'pear', 'apple'}
print('orange' in mi_conjunto)  # Salida: True
print('crabgrass' in mi_conjunto)  # Salida: False

# Creación de conjunto mediante set()
a = set()  # Crea un conjunto vacío
print(type(a))  # Salida: <class 'set'>


# Comparación de creación de conjunto desde una palabra
conjunto_letras = set('abracadabra')  # Crea un conjunto con todas las letras únicas de la palabra
conjunto_palabra = {'abracadabra'}  # Crea un conjunto con un solo elemento
print(conjunto_letras)  # Salida: {'r', 'b', 'd', 'c', 'a'}
print(conjunto_palabra)  # Salida: {'abracadabra'}
print(type(conjunto_letras), type(conjunto_palabra))  # Salida: <class 'set'> <class 'set'>

# La función set() recibe un solo argumento
mi_conjunto = set(['apple', 'pear', 'apple'])  # Recibe una lista y la transforma en un conjunto
print(mi_conjunto)  # Salida: {'pear', 'apple'}
```

### Construcción por Comprensión

De forma similar a las comprensiones de listas, los conjuntos también soportan la comprensión.

```python
# Construcción de un conjunto utilizando comprensión
mi_conjunto = {x for x in 'abracadabra'}
print(mi_conjunto)  # Salida {'r', 'c', 'a', 'b', 'd'}

# Otro ejemplo
mi_conjunto = {x for x in 'abracadabra' if x not in 'abc'}
print(mi_conjunto)  # Salida {'r', 'd'}
```

### Operaciones

Los conjuntos soportan operaciones matemáticas como la unión`|`, intersección`&`, diferencia `-`, y diferencia simétrica `^`.

También soportan los operadores `in` y `not in`.

```python
# Operaciones con conjuntos
# Debes notar que la salida no siempre se muestran en el mismo orden si ejecutas varias veces el programa
a = set('abracadabra')
b = set('alacazam')

# Letras únicas en los conjuntos
print(a)  # Salida: {'r', 'b', 'd', 'c', 'a'}
print(b)  # Salida: {'l', 'a', 'c', 'm', 'z'}

# Diferencia: letras únicas en 'a' pero no en 'b'
print(a - b)  # Salida: {'r', 'd', 'b'}

# Unión: letras en 'a' o 'b' o en ambas
print(a | b)  # Salida {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

# Intersección: letras en 'a' y 'b'
print(a & b)  # Salida: {'a', 'c'}

# Diferencia Simétrica: letras en 'a' o 'b' pero no en ambas
print(a ^ b)  # Salida: {'r', 'd', 'b', 'm', 'z', 'l'}
```

## Casos especiales

### Colas

#### Recordemos

Las colas se corresponden con FIFO (First Input, First Output).

#### Usando listas como colas

Si bien es posible usar una lista como una cola, donde el primer elemento añadido es el primer elemento retirado (primero en entrar, primero en salir); resulta que las listas no son eficientes para este propósito (refiriéndonos a optimización de proceso y memoria).

Agregar y sacar del final de la lista es rápido, pero insertar o sacar del comienzo de una lista es lento (porque todos los otros elementos tienen que ser desplazados por uno).

Para implementar una cola, utilizamos `collections.deque` que fue diseñado para añadir y quitar elementos de ambos extremos de forma óptima.


Sintaxis:

    deque([iterable[, maxlen]])

    donde:

	iterable  Son los elementos de la cola, si se omite se crea una deque vacía.

	maxlen	  Es el limite del largo de la deque, si se omite no tiene límite.

Por ejemplo:

```python
# Implementación de una cola utilizando listas y collections.deque
from collections import deque


# Creamos la cola
my_queue = deque(["Eric", "John", "Michael"])

# Agregamos elementos al final de la cola
my_queue.append("Terry")
my_queue.append("Graham")
print(my_queue)  # Salida: deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])

# Extraemos elementos del inicio de la cola
my_queue.popleft()
print(my_queue)  # Salida: deque(['John', 'Michael', 'Terry', 'Graham'])
my_queue.popleft()
print(my_queue)  # Salida: deque(['Michael', 'Terry', 'Graham'])

```


Como mencionamos arriba, `collections.deque` soporta agregar y quitar elementos desde ambos extremos de la lista con los métodos

```python
my_queue.appendleft('Jessica')
print(my_queue)  # Salida: deque(['Jessica', 'Michael', 'Terry', 'Graham'])
my_queue.pop()  # Remueve y devuelve el elemento del lado derecho de la cola 'Graham'

```

También soporta los siguientes métodos, entre otros:

```python
my_queue.insert(i, x)  # Inserta x en la posición i
my_queue.remove(value)  # Remueve la primer ocurrencia de value en la cola
my_queue.clear()  # Remueve todos los elementos de la cola
my_queue.reverse() 
my_queue.copy()
my_queue.count(x)  # Cuenta el número de elementos x en la cola
```

[Documentación oficial: collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)

### Pilas

#### Recordemos

Las Pilas se corresponden con LIFO (Last Input, First Output).

#### Usando listas como pilas

Los métodos de lista hacen que resulte muy fácil utilizar una lista como una pila.

Para agregar un elemento a la cima de la pila, utilizamos `append()`.

Para retirar un elemento de la cima de la pila, utilizamos `pop()` sin un índice explícito.

Por ejemplo:

```python
# Implementación de una pila utilizando listas
my_stack = [3, 4, 5]
print(my_stack)  # Salida: [3, 4, 5]

# Apilamos (agregamos) elementos utilizando .append()
my_stack.append(6)
my_stack.append(7)
print(my_stack)  # Salida: [3, 4, 5, 6, 7]

# Des-apilamos (sacamos) elementos utilizando .pop()
my_stack.pop()  # Elimina el último elemento 7
print(my_stack)  # Salida: [3, 4, 5, 6]
my_stack.pop()
print(my_stack)  # Salida: [3, 4, 5]
my_stack.pop()
print(my_stack)  # Salida: [3, 4]
```

> Nota: Pero, en esta implementación, dentro del código pueden realizar `insert` o `del` y de esa manera modifican nuestra pila. Y esto no es lo que queremos de una pila.

#### Implementando Pilas con Clases

Implementar pilas utilizando clases nos brinda las siguientes ventajas:

- Encapsula el contenido de la pila (aunque no del todo)
- Sobre el objeto solo se pueden ejecutar los métodos definidos.

```python
# Implementación de una Pila mediante una clase
class Pila:
    def __init__(self):  # Constructor de la clase
        self.__lista_pila = []  # Encapsulamos

    def push(self, value):
        self.__lista_pila.append(value)

    def pop(self):
        value = self.__lista_pila[-1]
        del self.__lista_pila[-1]
        return value


objeto_pila = Pila()

objeto_pila.push(3)
objeto_pila.push(2)
objeto_pila.push(1)

print(objeto_pila.pop())
print(objeto_pila.pop())
print(objeto_pila.pop())

''' Nota: Faltaría implementar un try/except para evitar el error que 
ocasionaría un pop() en una pila vacía.'''
```
