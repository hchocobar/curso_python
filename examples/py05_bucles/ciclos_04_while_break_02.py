numero_mayor = -99999999
contador = 0

# Sale del bucle con -1
while True:
    numero = int(input("Ingresa un número o escribe -1 para finalizar el programa:"))
    if numero == -1:
        break
    contador = 1
    if numero > numero_mayor:
        numero_mayor = numero

if contador != 0:
    print("El número más grande es", numero_mayor)
else:
    print("No ha ingresado ningún número")
