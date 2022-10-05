# 3. Condicionales

¿Cómo decidimos qué camino tomar en Python?

## 3.1.- Estructura if-elif-else

La sentencia `if` es una pregunta que, dependiendo del valor de la respuesta, nos permite hacer una u otra cosa (u otra más).

En python, una sentencia `if` se compone de un `if` seguido de una `condición` seguida de dos puntos `:`.

Las líneas siguientes deben formar un 'bloque' y si la respuesta a la condición es 'si' entonces se ejecutarán las sentencias del 'bloque'.

Recordemos los operadores relacionales o de comparación en Python que vimos la clase anterior. Los operadores de comparación se utilizan, como su nombre indica, para comparar dos o más valores. El resultado de estos operadores siempre es `True` o `False`.

Repasemos también  la PEP8: indentación que define una estructura de control o bloque que vimos en la primera clase.

Ejemplo:

```python
# Solicitamos el ingreso de un número
numero = input('Por favor, ingresa un número: ')
numero = int(numero)  # convertimos a entero el valor que ingresado
# Evaluamos el número y mostramos una leyenda de acuerdo a ese valor
if numero < 100:
    print('Hola')
elif numero < 200:
    print('Chao')
else:
    print('Adiós')
```

## Condicionales combinados

Las operaciones lógicas son expresiones matemáticas cuyo resultado es un valor booleano (verdadero o falso, true o false). Estas expresiones se utilizan principalmente en las estructuras de control.

En álgebra de Boole las operaciones básicas son tres y son la base para la programación en todos los lenguajes:

- **Y**: Producto lógico, puerta AND o función intersección.
- **O**: Suma lógica, puerta OR o función unión.
- **NO**: Negación lógica, puerta NOT o función complemento.

## Tablas de Verdad

Una Tabla de Verdad es un cuadro que muestra el valor de una proposición compuesta, para cada combinación que se pueda asignar a las expresiones que la forman.

No vamos a profundizar en este concepto, pero es importante mencionarlo y que comencemos a familiarizarnos con estas tablas y a continuación, te muestro el resultado de las tablas de verdad de las tres operaciones lógicas básicas.

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

## Ejercicios: Condicionales

1. Pedir la introducción de 2 números por teclado, luego comparar los números utilizando la ‘estructura de control condicional’ e imprimir en consola el resultado de las comparaciones.
2. Realizar un programa para una agencia de autos: Si el auto a la venta es un ford fiesta (código FFi), el descuento es de un 5%. Si el auto a la venta es un ford focus (código FFo), el descuento es del 10%. El usuario introduce el código del artículo y el programa saca el descuento correspondiente por pantalla.
3. Si un alumno tiene más de 18 años, Sí tiene acceso al portal web. (mostrar por pantalla: Bienvenido) Si un alumno NO tiene más de 18 años, NO tiene acceso al portal web.
