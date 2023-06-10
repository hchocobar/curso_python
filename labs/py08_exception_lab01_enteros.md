# LABORATORIO

## Enteros

**Tiempo Estimado:**
15-25 minutos

**Nivel de dificultad:**
Mediano

**Objetivos**

- Mejorar las habilidades del alumno para definir funciones.
- Utilizar excepciones para proporcionar un entorno de entrada seguro.

**Escenario**

Tu tarea es escribir una función capaz de ingresar valores enteros y verificar si están dentro de un rango
especificado.

La función debe:

- Aceptar tres argumentos: una entrada, un límite inferior aceptable y un límite superior aceptable.

- Si el usuario ingresa una cadena que no es un valor entero, la función debe emitir el mensaje `Error: entrada
incorrecta`, y solicitará al usuario que ingrese el valor nuevamente.

- Si el usuario ingresa un número que está fuera del rango especificado, la función debe emitir el mensaje `Error: el
valor no está dentro del rango permitido (min..max)` y solicitará al usuario que ingrese el valor nuevamente.

- Si el valor de entrada es válido, será regresado como resultado.

**Datos de prueba**

Prueba tu código cuidadosamente.
Así es como la función debería reaccionar ante la entrada del usuario:

    Ingresa un número entre -10 a 10: 100
    Error: el valor no está dentro del rango permitido (-10..10)
    
    Ingresa un número entre -10 a 10: asd
    Error: entrada incorrecta
    
    Ingresa un número entre -10 a 10: 1
    El número es: 1

**Código propuesto**

```python
def read_int(prompt, min, max):
    # Tu código aquí
    pass


v = read_int("Ingresa un numero de -10 a 10: ", -10, 10)

print("El número es:", v)

```
