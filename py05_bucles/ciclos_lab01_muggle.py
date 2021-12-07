""" LABORATORIO 3.1.2.3

Tiempo estimado
15 minutos

Nivel de dificultad
Fácil

Objetivos
Familiarizar al estudiante con:
- Utilizar el ciclo while.
- Reflejar situaciones de la vida real en código de computadora.

Escenario

Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada número_secreto. Quiere que todos
los que ejecutan su programa jueguen el juego Adivina el número secreto, y adivina qué número ha elegido para ellos.
¡Quienes no adivinen el número quedarán atrapados en un ciclo sin fin para siempre! Desafortunadamente, él no sabe
cómo completar el código.

Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

- Pedirá al usuario que ingrese un número entero.

- Utilizará un ciclo while.

-Comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el número
elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás
atrapado en mi ciclo!"  y se le solicitará que ingrese un número nuevamente. Si el número ingresado por el usuario
coincide con el número escogido por el mago, el número debe imprimirse en la pantalla, y el mago debe decir las
siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora".

¡El mago está contando contigo! No lo decepciones.


INFO EXTRA

Por cierto, mira la función print(). La forma en que lo hemos utilizado aquí se llama impresión multilínea. Puede
utilizar comillas triples para imprimir cadenas en varias líneas para facilitar la lectura del texto o crear un
diseño especial basado en texto. Experimenta con ello.
"""
numeroSecreto = 777

print(
    """
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
# Aquí escribe tu código
number = 0
while numeroSecreto != number:
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    number = int(input("ingresa un número entero para liberarte: "))
print("¡Bien hecho, muggle! Eres libre ahora")
