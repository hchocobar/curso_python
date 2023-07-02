# Se puede utilizar la técnica de argumentos con palabras clave para asignar valores predefinidos a los argumentos
def nombre(nombre3, apellido="Pérez"):
    print(nombre3, apellido)


def presentar(primer_nombre, segundo_nombre):
    print("Hola, mi nombre es", primer_nombre, segundo_nombre)


nombre("Andres")  # Salida: Andres Pérez
nombre("Betina", "Rodríguez")  # Salida: Betina Rodriguez

presentar(primer_nombre="James", segundo_nombre="Bond")
presentar(segundo_nombre="Skywalker", primer_nombre="Luke")
