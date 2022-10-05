# solicitamos tres números
numero1 = int(input("Ingresa el primer número:"))
numero2 = int(input("Ingresa el segundo número:"))
numero3 = int(input("Ingresa el tercer número:"))

# asumimos temporalmente que el primer número es el más grande
mas_grande = numero1

# comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario
if numero2 > mas_grande:
    mas_grande = numero2

# comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario
if numero3 > mas_grande:
    mas_grande = numero3

# imprimir el resultado
print("El número más grande es:", mas_grande)
