# Variante más avanzada de la instrucción para tratar varias excepciones
try:
    foo = int(input("Ingresa un número entero: "))
    bar = 1 / foo
    print(bar)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Ups! algo salio mal...")

print("The End")
