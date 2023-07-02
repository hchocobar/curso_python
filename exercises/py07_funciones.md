# Ejercicios

## Funciones

### Ejercicio 1

La función `input()` es un ejemplo de:

1. una función definida por el usuario
2. una función integrada


    Respuesta: es una función integrada

### Ejercicio 2

¿Qué ocurre cuando se invoca una función antes de ser definida? Ejemplo:

```python
hola()

def hola():
    print("hola!")

```

    Respuesta: Se genera una excepción (la excepción NameError)

### Ejercicio 3

¿Qué es lo que ocurrirá cuando se ejecute el siguiente código?

```python
def hola():
    print("hola")

    
hola(5)
```

    Respuesta: 
    Se genera una excepción (la excepción TypeError) - la función hola() no toma argumentos.

### Ejercicio 4

¿Cuál es la salida del siguiente código?

```python
def introduce_yourself(a="James", b="Bond"):
    print("Mi nombre es", b + "!", a, b + "!")


intro_yourself()
```

    Salida: Mi nombre es Bond! James Bond!

### Ejercicio 5

¿Cuál es la salida del siguiente código?

```python
def introduce_yourself(a="James", b="Bond"):
    print("Mi nombre es", b + "!", a, b + "!")


intro_yourself(b="López")
```

    Salida: Mi nombre es López! James López!

### Ejercicio 6

¿Cuál es la salida del siguiente fragmento de código?
```python
def introduce_yourself(a="James", b="Bond"):
    print("Mi nombre es", b + "!", a, b + "!")


intro_yourself("Susan")
```

    Salida: Mi nombre es Bond! Susan Bond!.

### Ejercicio 7

¿Cuál es la salida del siguiente código?

```python
def suma(a, b=2, c):
    print(a + b + c)

    
suma(a=1, c=3)
```

    Salida:
    SyntaxError - a non-default argument (c) follows a default argument (b=2)

## Return / None

### Ejercicio 1

¿Cuál es la salida del siguiente fragmento de código?

```python
def hola():
    return
    print("¡Hola!")

    
hola()
```

    Respuesta: La función devolverá un valor None implícito

### Ejercicio 2

¿Cuál es la salida del siguiente fragmento de código?

```python
def is_integer(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False 

    
print(is_integer(5))
print(is_integer(5.0))
print(is_integer("5"))
```

    Salidas:
    True
    False
    None

### Ejercicio 3

¿Cuál es la salida del siguiente fragmento de código?

```python
def even_numbers(stop):
    even_list = []
    for number in range(stop):
        if number % 2 == 0:
            even_list.append(number)
    return even_list


print(even_numbers(11))
```

    Salida:
    [0, 2, 4, 6, 8, 10] 

### Ejercicio 4

¿Cuál es la salida del siguiente fragmento de código?

```python
def squares_list(numbers):
    result = []
    for element in numbers:
        element **= 2
        result.append(element)
    return result


my_list = [1, 2, 3, 4, 5]
print(squares_list(my_list))
```

    Respuesta:
    [1, 4, 9, 16, 25]

## Alcances (Scope)

### Ejercicio 1

¿Qué ocurrirá cuando se intente ejecutar el siguiente código?

```python
def message():
    age = 18
    print("Hola, mundo!")

    
print(age)
```

    Respuesta:
    Se arrojará una excepción NameError:
    NameError: name 'age' is not defined

### Ejercicio 2

¿Cuál es la salida del siguiente fragmento de código?

```python
age = 18

def foo():
    age = 21
    print(age)

    
foo()
print(age)

```

    Salida:
    21
    18

### Ejercicio 3

¿Cuál es la salida del siguiente fragmento de código?

```python
age = 18

def foo():
    global age
    age = 21
    print(age)

    
foo()
age = 35
print(age)
```

    Salida:
    21
    35

### Ejercicio 4

¿Cuál es la salida del siguiente fragmento de código?

```python
age = 18

def foo():
    global age
    age = 21
    print(age)

    
age = 35
foo()
print(age)
```

    Salida:
    21
    21
