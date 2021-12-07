"""LABORATORIO

Tiempo Estimado
10-15 minutos

Nivel de Dificultad
Fácil

Objetivos
- Familiarizarse con los conceptos de números, operadores y operaciones aritméticas en Python.
- Realizar cálculos básicos.

Escenario Observa el código en el editor: lee un valor flotante, lo coloca en una variable llamada x, e imprime el
valor de la variable llamada y. Tu tarea es completar el código para evaluar la siguiente expresión:

3x3 - 2x2 + 3x - 1
(lease: 3 por x al cubo menos 2 por x al cuadrado mas 3 por x menos 1)

El resultado debe ser asignado a y.

Recuerda que la notación algebraica clásica muy seguido omite el operador de multiplicación, aquí se debe de incluir
de manera explicita. Nota como se cambia el tipo de dato para asegurarnos de que x es del tipo flotante.

Mantén tu código limpio y legible, y pruébalo utilizando los datos que han sido proporcionados. No te desanimes por
no lograrlo en el primer intento. Se persistente y curioso.


Prueba de Datos
Datos de Muestra

x = 0
x = 1
x = -1

Salida Esperada

y = -1.0
y = 3.0
y = -9.0

Código propuesto:
# codifica aquí tus datos de prueba.
x = float(x)
# escribe tu código aquí.
print("y =", y)
"""
# codifica aquí tus datos de prueba.
x = input("ingrese el valor de x: ")
x = float(x)
# escribe tu código aquí.
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
print("y =", y)
