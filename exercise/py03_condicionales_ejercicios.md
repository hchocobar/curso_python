# Ejercicios: Condicionales

## Ejercicios simples
1. Pedir la introducción de dos números por teclado, luego comparar los números utilizando la ‘estructura de control condicional’ e imprimir en consola el resultado de las comparaciones.
2. Realizar un programa para una agencia de automóviles: Si el automóvil en venta es un ford fiesta (código FFi), aplicarle un descuento es de un 5% al precio de venta. Si el automóvil a la venta es un ford focus (código FFo), el descuento a aplicar es del 10%. El usuario introduce el código del artículo y el programa calcula el descuento correspondiente y lo muestra por consola.
3. Si el alumno tiene más de 18 años, entonces tiene acceso al portal web. (mostrar por pantalla: "Bienvenido") Si el alumno NO tiene más de 18 años, entonces NO tiene acceso al portal web (mostrar por pantalla: "No tiene acceso").
4. Solicitar la edad al usuario. Validar que la edad ingresada no sea inferior a un año ni mayor a 120 años. Luego, si la edad es mayor que 18 años, imprimir en pantalla: "Tiene permiso de acceso".

## Cálculo de tiempo restante

**Escenario**

La tarea es preparar un código simple determinar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. Las horas se encuentran en el rango de 0 a 23 y los minutos de 0 a 59. La duración del evento exprésala en minutos. El resultado debe ser mostrado en la consola.

Por ejemplo, si el evento comienza a las 12:17 y su duración es de 59 minutos, terminará a las 13:16.

Prueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito.

**Datos de Prueba 1**

    Entrada de muestra:
        hora de inicio: 12 
        minuto de incio: 17 
        duración: 59
    Salida esperada: 13:16

**Datos de Prueba 2**

    Entrada de muestra:
        hora de inicio: 23 
        minuto de incio: 58 
        duración: 642
    Salida esperada: 10:40

**Datos de Prueba 3**

    Entrada de muestra:
        hora de inicio: 0 
        minuto de incio: 1 
        duración: 2939
    Salida esperada: 1:0

**Código de inicio propuesto**

```python
hora = int(input("Hora de inicio (horas): "))
minuto = int(input("Minuto de inicio (minutos): "))
duración = int(input("Duración del evento (minutos): "))
# Coloca tu código aquí
```

## Encontremos el mayor de los tres números.

Suponemos que el primer valor es el más grande. Luego verificamos esta hipótesis con los dos valores restantes.
Observa el siguiente código:

```python
# Lee tres números
numero_1 = int(input("Ingresa el primer número:"))
numero_2 = int(input("Ingresa el segundo número:"))
numero_3 = int(input("Ingresa el tercer número:"))

# Asumimos temporalmente que el primer número es el más grande
mas_grande = numero_1

# Comprobamos si el segundo número es más grande que el mayor número actual
if numero_2 > mas_grande:
    mas_grande = numero_2  # Actualizamos el número más grande si es necesario

# Comprobamos si el tercer número es más grande que el mayor número actual
if numero_3 > mas_grande:
    mas_grande = numero_3  # Actualizamos el número más grande si es necesario

# Imprimimos el resultado
print("El número más grande es:", mas_grande)

```
