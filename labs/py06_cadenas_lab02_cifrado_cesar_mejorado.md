# LABORATORIO

## Cifrado Cesar mejorado

**Tiempo Estimado:**
30-45 minutos

**Nivel de Dificultad:**
Difícil

**Prerrequisitos:**
- py06_cadenas_demo01_cifrado_cesar.py 
- py06_cadenas_demo02_descifrado_cesar.py

**Objetivos**
- Mejorar las habilidades del alumno para manipular cadenas.
- Convertir caracteres en código ASCII y viceversa.

**Escenario**

Ya estás familiarizado con el cifrado César, y es por eso que queremos que mejores el código que te mostramos
recientemente.

El cifrado César original cambia cada caracter por otro:
- a se convierte en b, z se convierte en a, y así sucesivamente.
- entonces el valor de desplazamiento es igual a 1.
 
Hagámoslo un poco más difícil y permitamos que el valor de desplazamiento pueda ser cualquier número 
en el rango de 1 a 25.

Además, dejemos que el código conserve las mayúsculas y minúsculas (las minúsculas permanecerán en minúsculas) y
todos los caracteres no alfabéticos deben permanecer intactos.

Tu tarea es escribir un programa el cual:

- Solicite al usuario una línea de texto para encriptar.
- Solicite al usuario un valor de desplazamiento (un número entero entre 1 y 25).
- Imprime el texto codificado.

**Nota:** Debes obligar al usuario a ingresar un valor de desplazamiento válido 
(¡no te rindas y no dejes que los datos incorrectos te engañen!).

**Datos de Prueba 1**

    Entrada Muestra: 
    abcxyzABCxyz 123
    valor de desplazamiento: 
    2
    Salida Muestra:
    cdezabCDEzab 123

**Datos de Prueba 2**
    
    Entrada Muestra: 
    The die is cast
    valor de desplazamiento: 
    25
    Salida Muestra:    
    Sgd chd hr bzrs
