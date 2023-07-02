# Módulos

<!-- TOC -->
* [Módulos](#módulos)
  * [Módulos de Python](#módulos-de-python)
  * [Importando Módulos](#importando-módulos)
    * [Primer método de importación: `import`](#primer-método-de-importación-import)
    * [¿Qué es el namespaces?](#qué-es-el-namespaces)
    * [Segundo método de importación: `from` … `import`](#segundo-método-de-importación-from--import)
    * [Tercer método de importación: `*`](#tercer-método-de-importación-)
    * [La palabra reservada `as`](#la-palabra-reservada-as)
    * [La función `dir()`](#la-función-dir)
* [Todos los Módulos de Python](#todos-los-módulos-de-python)
  * [El módulo `math`](#el-módulo-math)
    * [Funciones trigonométricas](#funciones-trigonométricas)
    * [Funciones relacionadas con la exponenciación](#funciones-relacionadas-con-la-exponenciación)
    * [Funciones de propósito general](#funciones-de-propósito-general)
  * [El módulo `platform`](#el-módulo-platform)
<!-- TOC -->

## Módulos de Python

Junto con Python se entregan una gran cantidad de módulos. Todos estos módulos, junto con las funciones integradas, forman la **Biblioteca estándar de Python**. 

Puedes ver la lista completa de la Biblioteca estándar de Python en este [link](https://docs.python.org/3/library/index.html).

Los módulos se identifican por su **nombre** y cada módulo consta de **entidades**. 

Estas entidades pueden ser funciones, variables, constantes, clases y objetos. Si se sabe cómo acceder a un módulo en particular, se puede utilizar cualquiera de las entidades que almacena.

## Importando Módulos

### Primer método de importación: `import`

Para importar un módulo utilizamos la siguiente instrucción:

```python
import modulo
```

La cláusula contiene:

- La palabra reservada `import`.
- El nombre del módulo que se va a importar.

La instrucción puede colocarse en cualquier parte del código, pero debe estar antes del primer uso de cualquiera de las entidades del módulo.

```python
import math, sys
```

La instrucción importa dos módulos, primero `math` y luego `sys`.

### ¿Qué es el namespaces?

Un namespace es el espacio en el que existen algunos nombres y los nombres no entran en conflicto entre sí.

Dentro de un determinado namespace, cada nombre debe permanecer único.

### Segundo método de importación: `from` … `import`

En el segundo método, la sintaxis del `import` señala con precisión qué entidad (o entidades) del módulo son aceptables en el código:

```python
from math import pi
```

La instrucción consta de los siguientes elementos:
- La palabra reservada `from`.
- El nombre del módulo a ser (selectivamente) importado.
- La palabra reservada `import`.
- El nombre o lista de nombres de la entidad o entidades las cuales están siendo importadas al namespace.

La instrucción tiene este efecto:

- Las entidades listadas son las únicas que son importadas del módulo indicado.
- Los nombres de las entidades importadas pueden ser accedidas dentro del programa.

### Tercer método de importación: `*`

En el tercer método, la sintaxis del `import` es una forma más agresiva que la presentada anteriormente:

```python
from module import *
```

El nombre de una entidad (o la lista de nombres de entidades) se reemplaza con un solo asterisco `*`.

### La palabra reservada `as`

El **aliasing** (renombrado) hace que el módulo se identifique con un nombre diferente al original.
La creación de un alias se realiza junto con la importación del módulo, y exige la siguiente forma de la instrucción import:

```python
import modulo as alias
```

- `modulo` identifica el nombre del módulo original 
- mientras que `alias` es el nombre que se desea usar en lugar del original.

A su vez, cuando usa la variante `from modulo import nombre` y se necesita cambiar el nombre de la entidad, se crea un alias para la entidad.

```python
from modulo import nombre as alias
```

La frase `nombre as alias` puede repetirse separadas por comas.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification as m_class, make_blobs as m_blobs

```

###  La función `dir()`

La función `dir()` devuelve una lista ordenada alfabéticamente que contiene todos los nombres de las entidades disponibles en el módulo.

# Todos los Módulos de Python

Hemos cubierto los conceptos básicos de los módulos de Python. Los módulos de Python conforman su propio universo, en el que Python es solo una galaxia, y nos aventuraríamos a decir que explorar las profundidades de estos módulos puede llevar mucho más tiempo que familiarizarse con Python "puro".


Puedes leer sobre todos los módulos estándar de Python [aquí](https://docs.python.org/3/py-modindex.html).

Además, la comunidad de Python en todo el mundo crea y mantiene cientos de módulos adicionales utilizados en aplicaciones muy específicas como genética, psicología o incluso astrología.

Estos módulos no están (y no serán) distribuidos junto con Python, o a través de canales oficiales, lo que hace que el universo de Python sea más amplio, casi infinito.

## El módulo `math`

### Funciones trigonométricas

```python
sin(x)  # Seno de x.
cos(x)  # Coseno de x.
tan(x)  # Tangente de x.
asin(x)  # Arcoseno de x.
acos(x)  # Arcocoseno de x.
atan(x)  # Arcotangente de x.

pi  # Constante con un valor que es una aproximación de π.
radians(x)  # Función que convierte x de grados a radianes.
degrees(x)  # Función que convierte x de radianes a grados.

sinh(x)  # Seno hiperbólico.
cosh(x)  # Coseno hiperbólico.
tanh(x)  # Tangente hiperbólica.
asinh(x)  # Arcoseno hiperbólico.
acosh(x)  # Arcocoseno hiperbólico.
atanh(x)  # Arcotangente hiperbólica

```

### Funciones relacionadas con la exponenciación

```python
e  # Constante con un valor que es una aproximación del número de Euler (e).

exp(x)  # Devuelve e elevado a la potencia x.
log(x)  # Logaritmo natural de x.
log(x, b)  # Logaritmo de x con base b.
log10(x)  # Logaritmo decimal de x (más preciso que log(x, 10)).
log2(x)  # Logaritmo binario de x (más preciso que log(x, 2)).
```

### Funciones de propósito general

```python
ceil(x)  # Devuelve el entero más pequeño mayor o igual que x.
floor(x)  # Devuelve el entero más grande menor o igual que x.
trunc(x)  # Devuelve el valor de x truncado a un entero.
factorial(x)  # Devuelve x! (x debe ser un valor entero y no negativo)
hypot(x, y)  # Devuelve la longitud de la hipotenusa de un triángulo rectángulo cuyas longitudes de catetos son x e y. 
             # Equivale a sqrt(pow(x, 2) + pow(y, 2)) pero más preciso.

random()  # Produce un número flotante en el rango (0.0 <= x < 1.0)
seed()  # Establece la semilla con la hora actual
seed(int_value)  # Establece la semilla con el valor entero int_value

randrange(fin)  # Genera un valor entero en el rango
randrange(inico, fin)   # Genera un valor entero en el rango
randrange(inicio, fin, incr)   # Genera un valor entero en el rango

randint(izquierda, derecha)  # Genera un valor entero en el rango [izquierda, derecha] (incluye el lado derecho)

choice(secuencia)  # Elige un elemento aleatorio de la secuencia de entrada y lo devuelve

```

## El módulo `platform`

El módulo platform permite acceder a los datos de la plataforma subyacente, es decir, hardware, sistema operativo e información sobre la versión del intérprete.

```python
# La función muestra todas las capas subyacentes en un solo vistazo
platform(aliased = False, terse = False)

machine()  # Nombre genérico del procesador
processor()  # Nombre real del procesador (si fuese posible)
system()  # Nombre genérico del sistema operativo
version()  # Versión del sistema operativo
python_implementation()  # Devuelve la implementación de Python
python_version_tuple()  # Devuelve una tupla de tres elementos
                        # - la parte mayor de la versión de Python
                        # - la parte menor,
                        # - el número de nivel del patch.

```
