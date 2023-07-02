# Funciones

<!-- TOC -->
* [Funciones](#funciones)
  * [Definición](#definición)
  * [Tipos de funciones básicas en Python](#tipos-de-funciones-básicas-en-python)
  * [Invocando a una función](#invocando-a-una-función)
  * [Funciones definidas por el usuario](#funciones-definidas-por-el-usuario)
  * [Parámetros y Argumentos](#parámetros-y-argumentos)
    * [Parámetros](#parámetros)
    * [Argumentos](#argumentos)
    * [Técnicas para pasar argumentos a una función](#técnicas-para-pasar-argumentos-a-una-función)
      * [Paso de argumentos posicionales](#paso-de-argumentos-posicionales-)
      * [Paso de argumentos con palabras clave](#paso-de-argumentos-con-palabras-clave-)
      * [Mix de argumentos posicionales y con palabras clave](#mix-de-argumentos-posicionales-y-con-palabras-clave)
      * [Valores por defecto](#valores-por-defecto)
  * [Return / None](#return--none)
    * [Sentencia `return`](#sentencia-return)
    * [Palabra reservada `None`](#palabra-reservada-none)
    * [Asignación del resultado de una función](#asignación-del-resultado-de-una-función)
    * [Listas como argumentos de funciones](#listas-como-argumentos-de-funciones)
    * [Listas como resultado de una función](#listas-como-resultado-de-una-función)
  * [Alcances (Scope) / `global`](#alcances-scope--global)
  * [Alcance y Argumentos](#alcance-y-argumentos)
    * [Argumentos Escalares](#argumentos-escalares)
    * [Argumentos Listas](#argumentos-listas)
<!-- TOC -->


## Definición

Una función es un bloque de código que realiza una tarea específica cuando la función es llamada (invocada). Las funciones son útiles para hacer que el código sea reutilizable, mejor organizado y más legible. Las funciones contienen parámetros y pueden regresar valores.

## Tipos de funciones básicas en Python

1. **Funciones integradas** las cuales son partes importantes de Python (ejemplo: la función `print()`). Puedes ver una lista completa de las funciones integradas de Python en la [documentación oficial](https://docs.python.org/3/library/functions.html).
2. **Funciones definidas por el usuario**, las cuales son escritas por los programadores para los programadores, puedes escribir tus propias funciones y utilizarlas libremente en tu código.
3. **Funciones de módulos preinstalados**.
4. **Las expresiones `lambda`**. Pequeñas funciones anónimas que pueden ser creadas con la palabra reservada `lambda`.

## Invocando a una función

El nombre de la función junto con los paréntesis y los argumentos, forman la invocación de la función.

`nombre_funcion(argumento)`

Cuando Python encuentra una invocación realiza lo siguiente:

- **Primero**, Python comprueba si el nombre especificado es legal (explora sus datos internos para encontrar la función con ese nombre; si esta búsqueda falla, Python cancela el código).
- **Segundo**, Python comprueba que el número de argumentos cumplan con los requisitos de la función y le permiten invocar la función de esta manera (por ejemplo, si una función específica exige exactamente dos argumentos, cualquier invocación que entregue solo un argumento se considerará errónea y abortará la ejecución del código).
- **Tercero**, Python deja el código por un momento y salta dentro de la función que se desea invocar; por lo tanto, también toma los argumentos y los pasa a la función.
- **Cuarto**, la función ejecuta el código, provoca el efecto deseado (si lo hubiera), evalúa el (los) resultado(s) deseado(s) y termina la tarea.
- **Finalmente**, Python regresa al código (al lugar inmediatamente después de la invocación) y reanuda su ejecución.

## Funciones definidas por el usuario

Las funciones propias se pueden definir utilizando la palabra reservada `def` y con la siguiente sintaxis:

```python
def my_function(parámetros_opcionales):  # Declaración de la función
    pass  # Cuerpo de la función


my_function(argumentos_opcionales)  # Invocación de la función

```

El nombre de la función debe ser significativo y se puede definir sin parámetros:

```python
def mensaje():
    print("Hola")

    
mensaje()

```

También, es posible definir funciones con parámetros:

```python
def hola(name):  # Declaración de la función
    print("Hola,", name)  # Cuerpo de la función


nombre = input("Ingresa tu nombre: ")
hola(nombre)  # Invocación de la función

```

## Parámetros y Argumentos

Las funciones pueden tener tantos parámetros como sean necesarios.

### Parámetros
Los **parámetros** solo existen dentro de las funciones (este es su entorno natural).

### Argumentos
Los **argumentos** existen fuera de las funciones, y son los que pasan los valores a los parámetros correspondientes.

### Técnicas para pasar argumentos a una función

Podemos pasar argumentos a una función utilizando las siguientes técnicas:

#### Paso de argumentos posicionales 

En esta técnica el orden de los parámetros es relevante.

```python
def resta(a, b):
    print(a - b)

    
resta(5, 2)    # Salida: 3
resta(2, 5)    # Salida: -3

```

#### Paso de argumentos con palabras clave 

En esta técnica el orden de los argumentos es irrelevante.

```python
def resta(a, b):
    print(a - b)

resta(a=5, b=2)    # Salida: 3
resta(b=2, a=5)    # Salida: 3
```

#### Mix de argumentos posicionales y con palabras clave

En esta técnica se especifican primero los argumentos posicionales y después los de palabras clave. Si se envían primero los de palabras claves, Python no lo ejecutará y marcará un error de sintaxis SyntaxError.

```python
def resta(a, b):
    print(a - b)

resta(5, b=2)  # Salida: 3
resta(5, 2)  # Salida: 3

```

#### Valores por defecto

Podemos utilizar la técnica de argumentos con palabras clave para asignar valores por defecto (predefinidos) a los argumentos:

```python
def nombre_completo(nombre, apellido="Pérez"):
    print(nombre, apellido)

nombre("Alicia", "Guijarro")  # Salida: Alicia Guijarro
nombre("Andrés")  # Salida: Andres Pérez

```

## Return / None

### Sentencia `return`

La instrucción `return` tiene dos variantes diferentes:

1. `return` sin una expresión
2. `return` con una expresión

Podemos emplear la palabra clave `return` para decirle a una función que devuelva algún valor. La instrucción return termina la función:

```python
def multiply(a, b):
    return a * b

print(multiply(3, 4))  # Salida: 12

```

### Palabra reservada `None`

`None` es una palabra reservada. Sus datos no representan un valor.

Solo hay dos tipos de circunstancias en las que None se puede usar de manera segura:

1. Cuando se le asigna a una variable (o se devuelve como el resultado de una función).
2. Cuando se compara con una variable para diagnosticar su estado interno.

```python
valor = None
if valor == None:
    print("Lo siento, no tienes ningún valor") 

```

Si una función no devuelve un cierto valor utilizando una cláusula de expresión `return`, se asume que devuelve implícitamente `None`.

```python
def multiply(a, b):
    return


print(multiply(3, 4))  # Salida: None

```

Observemos otro ejemplo:

```python
def my_function(n):
    if n % 2 == 0:
        return True


print(my_function(2))  # Salida: True
print(my_function(1))  # Salida: None

```

### Asignación del resultado de una función

El resultado de una función se puede asignar fácilmente a una variable, por ejemplo:

```python
def deseos():
    return "¡Feliz Cumpleaños!"


felicitaciones = deseos()
print(felicitaciones)  # Salida: ¡Feliz Cumpleaños!

```

Observa la diferencia en la salida en las siguientes invocaciones:
```python
def deseos():
    print("Mis deseos", end=" ")
    return "¡Feliz Cumpleaños!"


deseos()  # Salida: Mis deseos
print(deseos())  # Salida: Mis deseos ¡Feliz Cumpleaños!

```

### Listas como argumentos de funciones

Podemos utilizar una lista como argumento de una función:

```python
def hola_a_todos(my_list):
    for nombre in my_list:
        print("Hola,", nombre)

        
hola_a_todos(["Adam", "John", "Lucy"])

```

### Listas como resultado de una función

Podemos obtener una lista como resultado de función:

```python
def create_list(number):
    my_list = []
    for i in range(number):
        my_list.append(i)
    return my_list


print(create_list(5))  # Salida: [0, 1, 2, 3, 4]

```

## Alcances (Scope) / `global`

El alcance de un **nombre** es la parte del código donde el **nombre** es reconocido correctamente (por ejemplo, el nombre de una variable).

El alcance del parámetro de una función es la función en sí misma. El parámetro es inaccesible fuera de la función.

Una variable que existe fuera de una función tiene alcance dentro del cuerpo de la función, excluyendo a aquellas que tienen el mismo nombre (sombra).

```python
# Una variable que existe fuera de una función tiene alcance dentro del cuerpo de la función (ejemplo 1). 
# A menos que la función defina una variable con el mismo nombre (ejemplo 2 y ejemplo 3)

# Ejemplo 1:
number = 2
def my_function_01(x):
    return x * number


print(my_function_01(7))  # Salida: 14


# Ejemplo 2:
def my_function_02(x):
    number = 5
    return x * number

print(my_function_02(7))  # Salida: 35


# Ejemplo 3:
def my_function_03(x):
    number = 7
    return x * number

number = 3
print(my_function_03(7))  # Salida: 49

```

La palabra reservada `global` extiende el alcance de una variable incluyendo el cuerpo de las funciones para poder modificarlas (no solo leer los valores de las variables).
```python
def my_function():
    global number
    number = 7
    print("Valor dentro:", number)  # Salida: Valor dentro: 7 


number = 3
my_function()
print("Valor fuera:", number)  # Salida: Valor fuera: 7

```

## Alcance y Argumentos

### Argumentos Escalares

Cuando una función recibe el valor del argumento, no el argumento en sí.

```python
def my_function(number):
    print("Parámetro:", number)
    number += 1
    print("Parámetro incrementado", number)

    
mi_variable = 1
my_function(mi_variable)  # Pasa a la función como argumento
print("Argumento sin modificaciones", mi_variable)

```

### Argumentos Listas

Cuando el argumento es una lista, al cambiar el valor del parámetro (que recibe la lista) no cambiará la lista. 

```python
def my_function_with_list(foo):
    foo = foo[0] * 2
    return foo

    
numbers = [2, 3, 8]
my_function_with_list(numbers)
print(numbers)  # Salida: [2, 3, 8] 

```

Pero, si modificamos la lista identificada por el parámetro (Nota: ¡La lista no el parámetro!), la lista reflejará el cambio.

```python
def my_function_with_list(foo):
    del foo[0]

    
numbers = [2, 3, 8]
my_function_with_list(numbers)
print(numbers)  # Salida [3, 8]

```

> Recordemos: Las variables que contienen listas son almacenadas de manera diferente que las variables escalares.
