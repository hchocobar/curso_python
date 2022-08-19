""" Bloque finally:
El bloque finally siempre se ejecuta sin importar lo que sucedió antes, incluso cuando se genera o lanza una
excepción, sin importar si esta se ha manejado o no.
Nota: finally debe ser la última rama del código diseñada para manejar las excepciones.
Nota: else y finally no son dependientes entre sí, y pueden ocurrir de manera independiente. """


def mas_sobre_excepciones(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        return None
    else:
        print("Todo salió bien")
    finally:
        print("Finalmente adiós")
        return n


print(mas_sobre_excepciones(2))  # Salida: "Todo salió bien", "Finalmente adiós", 0.5
print(mas_sobre_excepciones(0))  # Salida: "División fallida", "Finalmente adiós", None
