# Variante más avanzada de la instrucción para tratar varias excepciones
try:
    x = int(input("Ingresa un numero entero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Ups! algo salio mal...")

print("THE END")
