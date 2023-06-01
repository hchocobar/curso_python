# El resultado de una función se puede asignar fácilmente a una variable, por ejemplo:
def deseos():
    return "¡Feliz Cumpleaños!"


d = deseos()
nombre = "Héctor"
print(d, nombre)  # Salida: ¡Feliz Cumpleaños! Héctor


# Observa la diferencia en la salida de estos dos ejemplos:
# Ejemplo 1
def deseos1():
    print("Mis deseos")  # Salida: "Mis deseos"
    return "¡Feliz Cumpleaños!"


deseos1()  # salida: Mis deseos


# Ejemplo 2
def deseos2():
    print("\nMis Deseos")  # Salida: "Mis deseos"
    return "¡Feliz Cumpleaños!"


d = deseos2()
print(d, nombre)  # Salida: ¡Feliz Cumpleaños!
