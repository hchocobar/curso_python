# Manejo básico de excepciones
try:
    print("1")
    foo = 1 / 0  # División por 0
    print("2")  # Esta línea no se ejecuta
except:
    print("Hemos producido un error intentando dividir por cero...")

print("3")
