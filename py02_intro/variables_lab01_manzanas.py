"""
LABORATORIO

Tiempo Estimado
10 minutos

Nivel de dificultad
Fácil

Objetivos
- Familiarizarse con el concepto de almacenar y trabajar con diferentes tipos de datos en Python.
- Experimentar con el código en Python.

Escenario
A continuación una historia:

Érase una vez en la Tierra de las Manzanas, Juan tenía tres manzanas, María tenía cinco manzanas, y Adán tenía seis
manzanas. Todos eran muy felices y vivieron por muchísimo tiempo. Fin de la Historia.

Tu tarea es:

1 Crear las variables: juan, maria, y adan.

2 Asignar valores a las variables. El valor debe de ser igual al numero de manzanas que cada quien tenía.

3 Una vez almacenados los números en las variables, imprimir el valor de las variables en una línea, y separar cada
una de ellas con una coma.

4 Después se debe crear una nueva variable llamada total_manzanas y se debe igualar a la suma de las tres variables
anteriores.

5 Imprime el valor almacenado en totalManzanas en la consola.

6 Experimenta con tu código: crea nuevas variables, asigna diferentes valores a ellas, y realiza varias operaciones
aritméticas con ellas (por ejemplo, +, -, *, /, //, etc.). Intenta poner una cadena con un entero juntos en la misma
línea, por ejemplo, "Numero Total de Manzanas:" y total_manzanas.

"""
juan = maria = adan = ""  # 1
# 2
juan = 3
maria = 5
adan = 6

print(juan, maria, adan, sep=",")  # 3
total_manzanas = juan + maria + adan  # 4
print(total_manzanas)  # 5
print("Número total de manzanas", total_manzanas)  # 6
