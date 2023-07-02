# Programa que lee una secuencia de números y cuenta cuántos números son pares y cuántos son impares
# El programa termina cuando se ingresa cero
impares = 0
pares = 0
print("Contaremos cuantos números Impares y pares ingresas por teclado")
numero = int(input("Introduce un número o escriba 0 para detener: "))  # Lee el primer número

# Termina la ejecución en 0
while numero != 0:
    # Verifica si el número es impar
    if numero % 2 == 1:
        # Aumenta el contador de números impares
        impares = impares + 1
    else:
        # Aumenta el contador de números pares
        pares += 1
    # Lee el siguiente número
    numero = int(input("Introduce un número o escriba 0 para detener:"))

# Imprime resultados
print("Números impares: ", impares)
print("Números pares: ", pares)
