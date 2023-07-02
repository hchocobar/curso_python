# Introducción

**Tabla de Contenidos**

<!-- TOC -->
* [Introducción](#introducción)
* [Instalaciones](#instalaciones)
  * [Python](#python)
  * [PyCharm](#pycharm)
* [Intérprete de Python](#intérprete-de-python)
* [PEPs - Python Enhancement Proposals](#peps---python-enhancement-proposals)
  * [PEP 8 - Style Guide for Python Code](#pep-8---style-guide-for-python-code)
    * [PEP 8: variables](#pep-8-variables)
    * [PEP 8: constantes](#pep-8-constantes)
    * [PEP 8: operadores](#pep-8-operadores)
    * [PEP 8: comentarios](#pep-8-comentarios)
    * [PEP 8: indentación](#pep-8-indentación)
<!-- TOC -->

Python es un lenguaje de programación.

- a high level language (un lenguaje de alto nivel),
  - lo opuesto sería un lenguaje de bajo nivel.
- an interpreted language (un lenguaje interpretado),
  - vs. compilado
- dynamically typed language (lenguaje de tipado dinámico).
  - vs. lenguaje fuertemente tipado.

Algunas de las características que lo hacen interesante para nosotros son:

    • Es fácil de utilizar.
    • Es un lenguaje “completo”; no sirve sólo para programar scripts.
    • Tiene gran variedad de estructuras de datos incorporadas al propio lenguaje.
    • Tiene una gran cantidad de bibliotecas (libraries).
    • Permite la 
        ◦ programación modular, 
        ◦ orientada a objetos y su uso 
        ◦ como un lenguaje imperativo tradicional.
    • Es interpretado. Esto facilita el desarrollo (aunque ralentice la ejecución).
    • Se puede utilizar desde un entorno interactivo.
    • Se puede extender fácilmente.
    • Es muy expresivo: un programa Python ocupa mucho menos que su equivalente en otros lenguajes.
 
# Instalaciones

## Python

Python ya suele estar instalado en sistemas linux. Si en tu sistema no está instalado entonces descargarlo del link oficial:

[Python](https://www.python.org/) | 
[Python Download](https://www.python.org/downloads/) |

## PyCharm

PyCharm es un IDE (Integrated Development Environment) que se utiliza específicamente para Python. 

Está desarrollado por la empresa checa JetBrains y puedes descargarlo y leer documentación en los siguientes enlaces:

[PyCharm](https://www.jetbrains.com/pycharm/) |
[Installation Guide](https://www.jetbrains.com/help/pycharm/installation-guide.html) | 


# Intérprete de Python

Python suele estar instalado en `/usr/local/bin` o en `/usr/bin`, ası́ que para invocar al intérprete interactivo debes abrir una terminal y escribir:

```terminal
$ python
```
o 
```terminal
$ python3
```
El sistema arrancará con un mensaje parecido a:
```terminal
Python 3.9.5 (default, May 11 2021, 08:20:37)
[GCC 10.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Esto nos permite empezar a trabajar (`>>>` es el prompt del intérprete). 

Para salir del intérprete interactivo tenemos que pulsar `Ctrl+D`.

# PEPs - Python Enhancement Proposals

Las PEPs son “propuestas de mejora de Python”.

Hay algunas que debemos conocer desde el inicio de nuestro aprendizaje.

[PEPs](https://www.python.org/dev/peps/) | 
[PEP 8](https://www.python.org/dev/peps/pep-0008/) |


## PEP 8 - Style Guide for Python Code

Una de ellas es la PEP8. A continuación vamos a listar algunos ejemplos (no todos):

### PEP 8: variables

Utilizar nombres descriptivos y en minúsculas. Para nombres compuestos, separar las palabras por guiones bajos.

```python
mi_variable = 12
```
Incorrectos:

		MiVariable = 12
		mivariable = 12
		miVariable = 12

### PEP 8: constantes

Utilizar nombres descriptivos y en mayúsculas separando palabras por guiones bajos. 

```python
MI_CONSTANTE = 12
```

### PEP 8: operadores

Siempre colocar un espacio en blanco, antes y después de un operador

```python
monto_bruto = 175
tasa_interes = 12
monto_interes = monto_bruto * tasa_interes / 100
tasa_bonificacion = 5
importe_bonificacion = monto_bruto * tasa_bonificacion / 100
monto_neto = (monto_bruto - importe_bonificacion) + monto_interes
```

### PEP 8: comentarios

Comentarios en la misma línea del código deben separarse con dos espacios en blanco. Luego del símbolo # debe ir un solo espacio en blanco  e iniciar con la primera letra en mayúscula. 

```python
a = 15  # Edad de María 
```

### PEP 8: indentación

Una indentación de 4 (cuatro) espacios en blanco, indicará que las instrucciones identadas, forman parte de una misma estructura de control o bloque.
```python
numero = 50
if numero < 100:
    print('Hola')
elif numero < 200:
    print('Chao')
else:
    print('Adiós')
```
