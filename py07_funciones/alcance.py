# Alcance - Scope
def saludo():
    print("Hola")
    print('estoy saludando')


def hola(nombre2):  # Definiendo una función
    print("Hola,", nombre2)  # cuerpo de la función
    nombre2 = "Nombre2"
    print('Hola', nombre)
    print("Hola,", nombre2)
    dia_interno = 'viernes'
    print(dia_interno)
    return nombre2


saludo()
nombre = input("Ingresa tu nombre: ")
dia = "miércoles"
otro_nombre = hola(nombre)
print(otro_nombre)
print(nombre)
print(dia)

# No existe en este scope la variable dia_interno
print(dia_interno)  # NameError: name 'dia_interno' is not defined
