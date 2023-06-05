# Laboratorio

**Escenario**

La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. Las horas van de 0 a 23 y los minutes de 0 a 59. El resultado debe ser mostrado en la consola.

Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

No te preocupes si tu código no es perfecto, está bien si acepta una hora invalida, lo más importante es que el código produzca una salida correcta acorde a la entrada dada.

**Código propuesto**

```python
hora_inicio = int(input("Hora de inicio (horas): "))
minuto_inicio = int(input("Minuto de inicio (minutos): "))
duración_del_evento = int(input("Duración del evento (minutos): "))

# Coloca tu código aquí
```

Pista: utilizar los operadores `%` y `//` puede ser clave para el éxito.

**Datos de Prueba**

    Entrada de muestra:
    12
    17
    59
    Salida esperada: 13:16
    
    Entrada de muestra:
    23
    58
    642
    Salida esperada: 10:40
    
    Entrada de muestra:
    0
    1
    2939
    Salida esperada: 1:0
