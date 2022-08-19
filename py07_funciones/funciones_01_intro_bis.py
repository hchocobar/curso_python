# Definimos funciones utilizando la palabra reservada def
# Podemos definir una función sin parámetros, con un parámetro o más
def saludo():
    print("Hola")


def hola(nombre2):  # definiendo una función con un parámetro
    print("Hola,", nombre2)  # cuerpo de la función
    print(dia)


def feliz_dia(dia3, nombre3):  # definiendo una función con dos parámetros
    print("Feliz", dia3, nombre3)  # cuerpo de la función


nombre = input("Ingresa tu nombre: ")
dia = input("Ingrese el día: ")

# Invocación de la función con el nombre de la función y paréntesis
# dentro de los cuales agregamos los argumentos (# opcional)
saludo()  # invoco una función sin argumentos
hola(nombre)  # invoco una función con un argumento
feliz_dia(nombre, dia)  # invoco una función con varios argumentos
