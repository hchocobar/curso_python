""" Bloque else:
El código que escribas en este bloque se ejecuta si, y solo sí, no se ha generado ninguna excepción dentro de la
parte del try:. Podemos decir que esta rama se ejecuta después del try: si no se ejecutó ningún except:.
Semánticamente podríamos leerlo como: Si ningún except se ejecuta, entonces ejecuta este código.
Nota: la rama else debe ubicarse después de la última rama except. """


def mas_sobre_excepciones(foo):
    try:
        foo = 1 / foo
    except ZeroDivisionError:
        print("División fallida")
        return None
    else:
        print("Todo salió bien")
        return foo


print(mas_sobre_excepciones(2))  # Salida: "Todo salió bien", 0.5
print(mas_sobre_excepciones(0))  # Salida: "División fallida", None
