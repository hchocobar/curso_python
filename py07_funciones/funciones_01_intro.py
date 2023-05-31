# Definimos funciones utilizando la palabra reservada def
# Podemos definir una función sin parámetros, con un parámetro o más
def saludo():
    print("Hola")


def hola(nombre2):  # Definiendo una función
    print("Hola,", nombre2)  # Cuerpo de la función


def feliz_dia(dia3, nombre3):  # Definiendo una función
    print("Feliz", dia3, nombre3)  # Cuerpo de la función


nombre = input("Ingresa tu nombre: ")
dia = input("Ingrese el día: ")

# Invocación de la función con el nombre de la función y paréntesis dentro de los cuales agregamos los argumentos.
saludo()  # Invoco una función sin argumentos
hola(nombre)  # Invoco una función con un argumento
feliz_dia(dia, nombre)  # Invoco una función con varios argumentos
