# PROYECTO

## Tic Tac Toe

**Tiempo estimado:**
30-60 minutos

**Nivel de dificultad:**
Medio / Difícil

**Objetivos**

- Perfeccionar las habilidades del estudiante al emplear Python para resolver problemas complejos.
- La integración de técnicas de programación en un solo programa consistente de varias partes.

**Escenario**

Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés, "tres en raya" o
"ta-te-ti") con el usuario.

Para hacerlo más fácil, Hemos decidido simplificar el juego. Aquí están nuestras reglas:
- La máquina (por ejemplo, el programa) jugará utilizando las 'X'.
- El usuario (por ejemplo, tú) jugará utilizando las 'O'.
- El primer movimiento es de la máquina: siempre coloca una 'X' en el centro del tablero.
- Todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia).
- El usuario ingresa su movimiento introduciendo el número de cuadro elegido. El número debe de ser válido,
por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado.
- El programa verifica si el juego ha terminado. Existen cuatro posibles veredictos: 
  - el juego continúa,
  - el juego termina en empate, 
  - tú ganas, o 
  - la máquina gana.
- La máquina responde con su movimiento y se verifica el estado del juego.
- No se debe implementar algún tipo de inteligencia artificial, la máquina elegirá un cuadro de manera aleatoria,
eso es suficiente para este juego.

El ejemplo del programa es el siguiente:

Juega la máquina:

| 1 | 2 | 3 |
|---|---|---|
| 4 | X | 6 |
| 7 | 8 | 9 |

Ingresa tu movimiento: 1

| O | 2 | 3 |
|---|---|---|
| 4 | X | 6 |
| 7 | 8 | 9 |

Juega la máquina:

| O | X | 3 |
|---|---|---|
| 4 | X | 6 |
| 7 | 8 | 9 |

Ingresa tu movimiento: 8

| O | X | 3 |
|---|---|---|
| 4 | X | 6 |
| 7 | O | 9 |

Juega la máquina:

| O | X | 3 |
|---|---|---|
| 4 | X | X |
| 7 | O | 9 |

Ingresa tu movimiento: 4

| O | X | 3 |
|---|---|---|
| O | X | X |
| 7 | O | 9 |

Juega la máquina:

| O | X | X |
|---|---|---|
| O | X | X |
| 7 | O | 9 |

Ingresa tu movimiento: 7

| O | X | X |
|---|---|---|
| O | X | X |
| O | O | 9 |

Juega la máquina:

    ¡Has Ganado!

**Requerimientos:**

Implementa las siguientes características:

- El tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres
elementos (la lista interna representa las filas) de manera que todos los cuadros puedas ser accedidos empleado la
siguiente sintaxis: `board[fila][columna]`
- Cada uno de los elementos internos de la lista puede contener 'O', 'X', o un dígito representando el número del
cuadro (si el cuadro tiene un dígito, entonces dicho cuadro se considera libre).
- La apariencia de tablero debe de ser igual a la presentada en el ejemplo.
- Implementa las funciones definidas para ti en el editor.

Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada `randrange()`.

El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios del 1 al 8).

```python
from random import randrange


for i in range(10):
    print(randrange(8))

```

**Código propuesto:**

```python
def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero y lo muestra en la consola
    pass


def enter_move(board):
    # Acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    # Verifica la entrada y actualiza el tablero de acuerdo a la decisión del usuario
    pass


def make_list_of_free_fields(board):
    # Examina el tablero y construye una lista de todos los cuadros vacíos 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
    pass


def victory_for(board, sign):
    # Analiza el estatus del tablero para verificar si el jugador que utiliza las 'O' o las 'X' ha ganado el juego
    pass


def draw_move(board):
    # Dibuja el movimiento de la máquina y actualiza el tablero
    pass

```
