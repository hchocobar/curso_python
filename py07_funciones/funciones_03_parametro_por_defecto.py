# Se puede utilizar la técnica de argumentos con palabras clave para asignar valores predefinidos a los argumentos
def nombre(nombre3, apellido="Pérez"):
    print(nombre3, apellido)


nombre("Andres")  # salida: Andres Pérez
nombre("Betina", "Rodríguez")  # salida: Betina Rodriguez


def presentar(primer_nombre, segundo_nombre):
    print("Hola, mi nombre es", primer_nombre, segundo_nombre)


presentar(primer_nombre="James", segundo_nombre="Bond")
presentar(segundo_nombre="Skywalker", primer_nombre="Luke")
