# 3. Condicionales

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

