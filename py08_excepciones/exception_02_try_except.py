# Manejo básico de excepciones
try:
    print("1")
    x = 1 / 0  # división por 0
    print("2")  # esta línea es saltada (no se ejecuta)
except:
    print("Hemos producido un error intentando dividir por cero...")


print("3")

# x = 1 / 0
