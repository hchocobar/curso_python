# programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares
# programa termina cuando se ingresa cero

numeros_impares = 0
numeros_pares = 0
print("Contaremos cuantos números Impares y pares ingresas por teclado")
# lee el primer número
numero = int(input("Introduce un número o escriba 0 para detener: "))

# 0 termina la ejecución
while numero != 0:
    # verificar si el número es impar
    if numero % 2 == 1:
        # aumentar el contador de números impares
        numeros_impares = numeros_impares + 1
    else:
        # aumentar el contador de números pares
        numeros_pares += 1
    # lee el siguiente número
    numero = int(input("Introduce un número o escriba 0 para detener:"))

# imprimir resultados
print("Números impares: ", numeros_impares)
print("Números pares: ", numeros_pares)
