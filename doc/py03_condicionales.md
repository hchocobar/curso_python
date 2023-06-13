# 3. Condicionales

<!-- TOC -->
* [3. Condicionales](#3-condicionales)
  * [3.1.- Estructura if-elif-else](#31--estructura-if-elif-else)
  * [Condicionales combinados](#condicionales-combinados)
  * [Tablas de Verdad](#tablas-de-verdad)
  * [Ejemplos](#ejemplos)
    * [Ejemplo 1](#ejemplo-1)
    * [Ejemplo 2](#ejemplo-2)
    * [Ejemplo 3](#ejemplo-3)
    * [Ejemplo 4](#ejemplo-4)
<!-- TOC -->

¿Cómo decidimos qué camino tomar en Python?

## 3.1.- Estructura if-elif-else

La sentencia `if` es una pregunta que, dependiendo del valor de la respuesta, nos permite hacer una u otra cosa (u otra más).

En python, una sentencia `if` se compone de un `if` seguido de una `condición` seguida de dos puntos `:`.

Las líneas siguientes deben formar un 'bloque' y si la respuesta a la condición es `True` entonces se ejecutarán las sentencias del 'bloque'.

Los operadores de comparación se utilizan, como su nombre indica, para comparar dos o más valores. El resultado de estos operadores siempre es `True` o `False`.

Recordemos también la **PEP8: indentación** que define una estructura de control o bloque.

Ejemplo:

```python
# Solicitamos el ingreso de un número
numero = input('Por favor, ingresa un número: ')
numero = int(numero)  # Convertimos a entero el valor ingresado

# Evaluamos el número y mostramos una leyenda de acuerdo a ese valor
if numero < 100:
    print('El número ingresado es menor a cien')
elif numero < 200:
    print('El número ingresado es mayor o igual que cien y menor que doscientos')
else:
    print('El número ingresado es mayor o igual que doscientos')

```

## Condicionales combinados

Las operaciones lógicas son expresiones matemáticas cuyo resultado es un valor booleano (verdadero o falso, true o false). Estas expresiones se utilizan principalmente en las estructuras de control.

En **álgebra de Boole** las operaciones básicas son tres y son la base para la programación en todos los lenguajes de programación:

- **Y** también denominado: producto lógico, puerta AND o función intersección.
- **O** también denominado: suma lógica, puerta OR o función unión.
- **NO** también denominado: negación lógica, puerta NOT o función complemento.

## Tablas de Verdad

Una Tabla de Verdad es un cuadro que muestra el valor de una proposición compuesta, para cada combinación que se pueda asignar a las expresiones que la conforman.

**Tabla de verdad de Y**: Producto lógico, puerta AND o función intersección.

|    expr1    |   expr2    |  expr1   Y  expr2  |
|:-----------:|:----------:|:------------------:|
|    Falso    |   Falso    |       Falso        |
|    Falso    | Verdadero  |       Falso        |
|  Verdadero  |   Falso    |       Falso        |
|  Verdadero  | Verdadero  |     Verdadero      |

**Tabla de verdad de O**: 
Suma lógica, puerta OR o función unión.

|   expr1   |   expr2   | expr1   O   expr2 | 
|:---------:|:---------:|:-----------------:|
|   Falso   |   Falso   |       Falso       |
|   Falso   | Verdadero |     Verdadero     |
| Verdadero |   Falso   |     Verdadero     |
| Verdadero | Verdadero |     Verdadero     |

**Tabla de verdad de NO**: Negación lógica, puerta NOT o función complemento

|   expr1   |  NO expr1   |
|:---------:|:-----------:|
|   Falso   |  Verdadero  |
| Verdadero |    Falso    |

## Ejemplos

### Ejemplo 1

```python
number_1 = int(input("Ingrese el primer número: "))
number_2 = int(input("Ingrese el segundo número: "))
number_3 = int(input("Ingrese el tercer número: "))
# Número mayor
if number_2 <= number_1 and number_1 >= number_3:
    print("El número mayor es: ", number_1)
elif number_2 > number_1 and number_2 > number_3:
    print("El número mayor es: ", number_2)
elif number_3 > number_1 and number_3 > number_1:
    print("El número mayor es: ", number_3)

```

### Ejemplo 2

```python
number = int(input("Ingrese un número: "))
if number < 0:  # Negativo
    print("El número es negativo")
elif number == 0:  # Cero
    print("El número es cero")
else:  # Positivo
    print("El número es positivo")
```

### Ejemplo 3

```python
number = int(input("Ingrese un número: "))
# Convertimos el número en positivo
if number < 0:
    number = number * -1
# Determinamos la cantidad de dígitos
if 0 <= number < 10:  # Un dígito
    print("El número tiene un dígito")
elif 10 <= number < 100:  # Dos dígitos
    print("El número tiene dos dígitos")
elif 100 <= number < 1000:  # Tres dígitos
    print("El número tiene tres dígitos")
elif number >= 1000:  # Más de tres dígitos
    print("El número tiene más de tres dígitos")

```

### Ejemplo 4

```python
preguntas = int(input("Ingrese la cantidad de preguntas: "))
correctas = int(input("Ingrese la cantidad de respuestas correctas: "))
# Porcentaje
porcentaje = float(correctas * 100) / preguntas
# Nivel
if porcentaje >= 90:
    print("Nivel Excelente")
elif 75 <= porcentaje < 90:
    print("Nivel medio")
elif 50 <= porcentaje < 75:
    print("Nivel regular")
elif porcentaje < 50:
    print("Nivel bajo")
print(porcentaje)

```
