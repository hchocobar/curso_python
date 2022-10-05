# Laboratorio

**Tiempo estimado**: 10-15 minutos

**Nivel de dificultad**: Fácil/Medio

**Objetivos**

Familiarizar al estudiante con:

- Utilizar la declaración if-elif-else.
- Encontrar la implementación adecuada de reglas definidas verbalmente.
- Emplear el código de prueba usando entrada y salida de muestra.

**Escenario**

Como seguramente sabrás, debido a algunas razones astronómicas, el año pueden ser bisiesto o común. Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.

Desde la introducción del calendario gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

- Si el número del año no es divisible entre cuatro, es un año común.
- De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
- De lo contrario, si el número del año no es divisible entre 400, es un año común.
- De lo contrario, es un año bisiesto.

**Código Propuesto**

Observa el código que te proponemos: solo lee un número de año y debe completarse con las instrucciones que implementan la prueba que acabamos de describir.

```python
año = int(input("Introduzca un año: "))

#
# Coloca tu código aquí.
#
```

El código debe mostrar uno de los dos mensajes posibles, que son `Año bisiesto` o `Año común`, según el valor ingresado.

Por ahora no hace falta verificar si el año ingresado cae en la era gregoriana o no.

Consejo: utiliza los operadores `!=` y `%`.


**Datos de prueba**

    Entrada de muestra: 2000
    Resultado esperado: Año bisiesto
    
    Entrada de muestra: 2015
    Resultado esperado: Año común
    
    Entrada de muestra: 1999
    Resultado esperado: Año común
    
    Entrada de muestra: 1996
    Resultado esperado: Año bisiesto
