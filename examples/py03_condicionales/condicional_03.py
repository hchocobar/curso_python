# Imprimir tic si es múltiplo de 3 y mostrar fin de programa
# Imprimir toc si es múltiplo de 5 y mostrar fin de programa
# Imprimir tictoc si es múltiplo de 3 y de 5 y luego mostrar fin de programa
numero = int(input('Por favor, ingresa un número: '))  # Solicitamos un número
if numero % 3 == 0 and numero % 5 == 0:
    print("ingresó un número múltiplo de 3 y de 5", numero)  # Verdadero
elif numero % 5 == 0:
    print('el número es múltiplo de 5', numero)
elif numero % 3 == 0:
    print('múltiplo de 3', numero)

print('Fin del programa')

if numero % 5 == 0:
    print('imprime siempre que sea múltiplo de 5')