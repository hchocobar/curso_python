"""LABORATORIO

Tiempo estimado
20 minutos

Nivel de dificultad
Intermedio

Objetivos
- Familiarizarse con los conceptos de números, operadores y expresiones aritméticas en Python.
- Comprender la precedencia y asociatividad de los operadores de Python, así como el correcto uso de los paréntesis.

Escenario

La tarea es completar el código para poder evaluar la siguiente expresión:

       1
-----------------
         1
x + -------------
            1
    x + ---------
              1
        x + -----
              x

El resultado debe de ser asignado a y. Se cauteloso, observa los operadores y priorízalos. Utiliza cuantos paréntesis
sean necesarios.

Puedes utilizar variables adicionales para acortar la expresión (sin embargo, no es muy necesario).Prueba tu código
cuidadosamente.

Datos de Prueba

Entrada de muestra: 1
Salida esperada:
y = 0.6000000000000001

Entrada de muestra: 10
Salida esperada:
y = 0.09901951266867294

Entrada de muestra: 100
Salida esperada:
y = 0.009999000199950014

Entrada de muestra: -5
Salida esperada:
y = -0.19258202567760344

Código Propuesto:
x = float(input("Ingresa el valor para x: "))
# coloca tu código aquí
print("y =", y)
"""
x = float(input("Ingresa el valor para x: "))
# coloca tu código aquí
y = 1 / (x + (1 / (x + (1 / (x + (1 / x))))))
print("y =", y)
