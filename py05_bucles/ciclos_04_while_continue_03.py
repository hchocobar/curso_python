numero_mayor = -99999999
contador = 0

numero = int(input("Ingresa un número o escribe -1 para finalizar el programa:"))

while numero != -1:
    if numero == -1:
        continue
    contador = 1
    if numero > numero_mayor:
        numero_mayor = numero
    numero = int(input("Ingresa un número o escribe -1 para finalizar el programa:"))

if contador:
    print("El número más grande es", numero_mayor)
else:
    print("No ha ingresado ningún número")
