# Introducción a Python

**Contenido**

- [Variables](#variables)
- [Tipos de datos](#tipos-de-datos)
- [Comentarios](#comentarios)
- [Operadores](#operadores)
  - [Operadores aritméticos](#operadores-aritmticos)
  - [Orden de las operaciones](#orden-de-las-operaciones-el-uso-de-los-parntesis)
  - [Operadores relacionales](#operadores-relacionales)
  - [Operadores lógicos](#operadores-lgicos)
  - [Operaciones lógicas y de bits](#operaciones-lgicas-y-de-bits)
  - [Operador de asignación vs. comparación](#operadores-de-asignacin-vs-comparacin)
- [Entrada de datos](#entrada-de-datos)
- [Salida de datos](#salida-de-datos)
- [Funciones integradas](#funciones-integradas)

## Variables

Una variable es un espacio para almacenar datos modificables, en la memoria.

Cada variable tiene un nombre y un valor. Este valor define el tipo de dato que contiene la variable.

Existe un tipo de “variable”, denominada constante, la cual se utiliza para definir valores fijos, que no requieran ser modificados.

Al nombrar una variable debes seguir las siguientes reglas:

- En nombre de la variable puede estar compuesto por 
  - letras, 
  - dígitos, y 
  - el carácter _ (guion bajo).
- El nombre de la variable debe comenzar con una letra.
  - El carácter guion bajo es considerado una letra.
- Las mayúsculas y minúsculas se tratan en forma distinta (case sensitive).
- El nombre de las variables no pueden ser igual a alguna palabra reservada de Python.
- Para variables utilizar nombres descriptivos y en minúsculas. Para nombres compuestos, separar las palabras por guiones bajos (PEP8)
- Para CONSTANTES utilizar nombres descriptivos y en MAYÚSCULAS. Para nombres compuestos, separar las palabras por guiones bajos (PEP8).

**Resumen**

1. Una variable es una ubicación nombrada, reservada para almacenar valores en la memoria.
2. Una variable es creada o inicializada automáticamente cuando se le asigna un valor por primera vez.
3. Cada variable debe de tener un nombre único (un identificador). 
   1. Un nombre válido debe ser aquel que no contiene espacios. 
   2. Debe comenzar con un guion bajo (_), o una letra. 
   3. No puede ser una palabra reservada de Python. 
   4. El primer carácter puede estar seguido de guiones bajos, letras, y dígitos. 
   5. Las variables en Python son sensibles a mayúsculas y minúsculas.
4. Python es un lenguaje de tipado dinámico, lo que significa que no se necesita declarar variables en él. Para asignar valores a las variables, se utiliza simplemente el operador de asignación, es decir el signo de igual `=`, por ejemplo: `foo = 1`.
5. También es posible utilizar operadores de asignación compuesta (operadores abreviados) para modificar los valores asignados a las variables, por ejemplo: `var += 1`, or `var -= 5`.
6. Se les puede asignar valores nuevos a variables ya existentes utilizando el operador de asignación o un operador abreviado: `var = 2`

## Tipos de datos

Una variable (o constante) puede contener valores de diversos tipos. Entre ellos:

```python
# Cadena de texto (string)
mi_cadena = "Hola Mundo!"

# Cadena multilínea
mi_cadena_multilinea = """
Esta es una cadena
de varias lineas """

# Números enteros
edad = 35
numero_grande = 35E8
numero_grande = 35e8
numero_octal = 0o35  # número entero octal
numero_octal = 0O35  # número entero octal
numero_hexa = 0x35  # número entero hexadecimal
numero_hexa = 0X35  # número entero hexadecimal

# Números reales
precio = 7435.28
precio = 74.
porcentaje = .4

# Booleano (verdadero / Falso)
verdadero = True
falso = False

# NonType – Ausencia de un valor
variable_vacia = None

# Existen además, otros tipos de datos más complejos, que veremos más adelante.
```

**Resumen**

1. Los **Literales** son notaciones para representar valores fijos en el código. Python tiene varios tipos de literales, es decir, un literal puede ser un número por ejemplo, 123), o una cadena (por ejemplo, "Yo soy un literal.").
2. El **Sistema Binario** es un sistema numérico que emplea 2 como su base. Por lo tanto, un número binario está compuesto por 0s y 1s únicamente, por ejemplo, 1010 es 10 en decimal.
3. Los sistemas de numeración **Octales y Hexadecimales** son similares pues emplean 8 y 16 como sus bases respectivamente. El sistema hexadecimal utiliza los números decimales más seis letras adicionales.
4. Los **Enteros** (o simplemente int) son uno de los tipos numéricos que soporta Python. Son números que no tienen una parte fraccionaria, por ejemplo, 256, o -1 (enteros negativos).
5. Los números **Punto-Flotante** (o simplemente flotantes) son otro tipo numérico que soporta Python. Son números que contienen (o son capaces de contener) una parte fraccionaria, por ejemplo: 1.27.
6. Para codificar un apóstrofe o comillas dentro de una cadena se puede utilizar el **carácter de escape**, por ejemplo, 'I\'m happy.', o abrir y cerrar la cadena utilizando un conjunto de símbolos distintos al símbolo que se desea codificar, por ejemplo, "I'm happy." para codificar un apóstrofe, y 'Él dijo "Python", no "typhoon"' para codificar comillas.
7. Los **Valores Booleanos** son dos objetos constantes Verdadero y Falso empleados para representar valores de verdad (en contextos numéricos 1 es True, mientras que 0 es False).
8. Existe un literal especial más utilizado en Python: el literal **None**. Este literal es llamado un objeto de NonType (ningún tipo), y puede ser utilizado para representar la ausencia de un valor.

## Comentarios

Un archivo, no solo puede contener código fuente. También puede incluir comentarios (notas que como programadores, indicamos en el código para poder comprenderlo mejor).

Los comentarios pueden ser de dos tipos: de una sola línea o multi-línea y se expresan de la siguiente manera:

```python
# Esto es un comentario de una sola línea

""" Y este es un comentario
de varias líneas """

# Este comentario es de una línea también
```

En los comentarios, pueden incluirse palabras que nos ayuden a identificar además, el subtipo de comentario:

```python
# TODO esto es algo por hacer
# FIXME esto es algo que debe corregirse
# XXX esto también, es algo que debe corregirse
```

## Operadores

### Operadores Aritméticos

Entre los operadores aritméticos que Python utiliza, podemos encontrar los siguientes:

| Símbolo  | Significado     | Ejemplo       | Como se lee                                        | Resultado |
|:--------:| --------------- | ------------- | -------------------------------------------------- | ---------:|
|    +     | Suma            | a = 10 + 5    | a es igual a 10 más 5                              | a es 15   |
|    -     | Resta           | a = 12 - 7    | a es igual 12 menos 7                              | a es 5    |
|    -     | Negación        | a = -5        | a es igual a menos 5                               | a es -5   |
|    *     | Multiplicación  | a = 7 * 5     | a es igual a 7 por 5                               | a es 35   |
|    **    | Potencia        | a = 2 ** 3    | a es igual a 2 al cubo                             | a es 8    |
|    /     | División        | a = 12.5 / 2  | a es igual a 12.5 dividido 2                       | a es 6.25 |
|    //    | División entera | a = 12.5 // 2 | a es igual a la división entera de 12.5 dividido 2 | a es 6.0  |
|    %     | Módulo          | a = 27 % 4    | a es igual al módulo de 27 dividido 4              | a es 3    |

### Orden de las Operaciones. El uso de los paréntesis

En los lenguajes de programación se utilizan los paréntesis para controlar lo que se conoce como el “Orden de las Operaciones”.

Una operación se define cuando se utiliza un operador (alguno de los sı́mbolos de la tabla anterior). Hay más operadores que esos sı́mbolos básicos, pero para esa lista (suma, resta, multiplicación y división), es suficiente con saber que la multiplicación y la división tiene mayor orden de prioridad que la suma y la resta. Esto significa que en una fórmula, la parte de la multiplicación o la división se calcula antes que la parte de la suma y resta.

A la siguiente fórmula:

```python
5 + 30 * 20  # resultado: 605
```

La resolvemos: _multiplicando 30 por 20, y luego sumamos 5 al resultado_ (se multiplica primero porque la multiplicación tiene mayor orden que la suma).

La siguiente fórmula muestra otro resultado:

```python
(5 + 30) * 20  # resultado: 700
```

Porque los paréntesis controlan el orden de las operaciones. Con los paréntesis, Python sabe que tiene que calcular primero todos los operadores que están dentro de los paréntesis, y luego los de fuera. Por eso esta fórmula se resuelve _sumando 5 a 30 y luego multiplicando el resultado por 20_.

#### Operadores y sus enlaces

Todos los operadores tienen enlazado hacia la izquierda, pero hay una excepción: la **potencia** tienen enlazado hacia la derecha.

#### Operadores unarios y binarios

La negación `-` es un operador unario porque necesita un solo operando (el símbolo positivo `+` también, pero en la práctica no es utilizado). 

Todos los otros operadores son binarios, porque necesitan dos operandos.

### Operadores Relacionales

Los operadores relacionales o de comparación se utilizan, como su nombre indica, para comparar dos o más valores. El resultado de estos operadores siempre es True o False.

| Operador | Descripción            | Verdadero o True                                                           | Falso o False     |
|:--------:|:----------------------:| -------------------------------------------------------------------------- | ----------------- |
|    ==    | igual                  | si el operando de la izquierda es igual que el de la derecha               | en caso contrario |
|    !=    | no igual o distinto de | si los operandos son distintos                                             | en caso contrario |
|    \>    | mayor que              | si el operando de la izquierda es estrictamente mayor que el de la derecha | en caso contrario |
|    <     | menor que              | si el operando de la izquierda es estrictamente menor que el de la derecha | en caso contrario |
|   \>=    | mayor o igual que      | si el operando de la izquierda es mayor o igual que el de la derecha       | en caso contrario |
|    <=    | menor o igual que      | si el operando de la izquierda es menor o igual que el de la derecha       | en caso contrario |

### Operadores Lógicos

Las operaciones lógicas son expresiones matemáticas cuyo resultado es un valor booleano (verdadero o falso, true o false). Estas expresiones se utilizan principalmente en las estructuras de control.

En álgebra de Boole las operaciones básicas son tres y son la base para la programación en todos los lenguajes:

- **Y** Producto lógico, puerta AND o función intersección
- **O**    Suma lógica, puerta OR o función unión
- **NO** Negación lógica, puerta NOT o función complemento

| Operador en Python | Significado | Lógica Proposicional | Funciones Lógicas | Electrónica, Hidraúlica | Conjuntos    |
|:------------------:|:-----------:|:--------------------:|:-----------------:|:-----------------------:|:------------:|
| `and`              | Y           | ^                    | Producto Lógico   | Puerta AND              | Intersección |
| `or`               | O           | ∨                    | Suma Lógica       | Puerta OR               | Unión        |
| `not`              | NO          | \~                   | Negación Lógica   | Puerta NOT              | Complemento  |

### Operaciones lógicas y de bits

1. Python es compatible con los siguientes operadores lógicos:
   1. and → si ambos operandos son verdaderos, la condición es verdadera, por ejemplo, (True and True) es True.
   2. or → si alguno de los operandos es verdadero, la condición es verdadera, por ejemplo, (True or False) es True.
   3. not → devuelve False si el resultado es verdadero y devuelve True si es falso, por ejemplo, not True es False.
2. Puedes utilizar operadores bit a bit para manipular bits de datos individuales. Los siguientes datos de muestra:
   1. `x = 15`, el cual es `0000 1111` en binario.
   2. `y = 16`, el cual es `0001 0000` en binario.

Se utilizarán para ilustrar el significado de operadores bit a bit en Python. Analiza los ejemplos a continuación:

    & hace un bit a bit and (y), por ejemplo, x & y = 0, el cual es 0000 0000 en binario.
    | hace un bit a bit or (o), por ejemplo, x | y = 31, el cual es 0001 1111 en binario.
    ˜ hace un bit a bit not (no), por ejemplo, ˜ x = 240, el cual es 1111 0000 en binario.
    ^ hace un bit a bit xor, por ejemplo, x ^ y = 31, el cual es 0001 1111 en binario.
    >> hace un desplazamiento bit a bit a la derecha, por ejemplo, y >> 1 = 8, el cual es 0000 1000 en binario.
    << hace un desplazamiento bit a bit a la izquierda, por ejemplo, y << 3 = , el cual es 1000 0000 en binario.

### Operadores de asignación vs. comparación

Importante: Asignación (=) vs. comparación (==)

Muy importante: No confundir el operador de comparar si son iguales (==) con la asignación (=) de un valor a una variable.

## Salida de datos

La función `print()` en Python

En Informática, la "salida" de un programa son los datos que el programa proporciona al exterior. Aunque en los inicios de la informática la salida más habitual era una impresora, hace muchos años que el dispositivo de salida más habitual es la pantalla de la computadora.

En los programas, para que Python nos muestre texto o variables hay que utilizar la función `print()`.

La barra invertida `\ ` tiene un significado muy especial cuando se usa dentro de las cadenas, es llamado el carácter de escape.

Argumentos de palabras clave: La función `print()` tiene dos argumentos de palabra clave: `end` y `sep`

## Entrada de datos

La función `input()`  permite a los usuarios introducir datos desde la entrada estándar (el teclado). La función `input()` siempre devuelve una cadena de texto.

La función input muestra el valor de ‘prompt’ -si es que se ha añadido como argumento de la función-, lee una línea desde la entrada estándar -el teclado-, la convierte en cadena de texto y la devuelve como resultado de la función.

De forma predeterminada, la función input() convierte la entrada en una cadena, aunque escribamos un número.

**Conversión de datos o casting**

Python ofrece dos simples funciones para especificar un tipo de dato y resolver este problema, aquí están: `int()` y `float()`.

- Si deseamos que Python interprete la entrada como un número entero, se debe utilizar la función `int()`.
- Si deseamos que Python interprete la entrada como un número decimal, se debe utilizar la función `float()`.

## Funciones integradas

También denominadas **funciones built-in**. El intérprete de Python tiene una serie de funciones y tipos incluidos en él que están siempre disponibles.

Tendrás un detalle de cada una de ellas en la [documentación oficial](https://docs.python.org/es/3.9/library/functions.html)