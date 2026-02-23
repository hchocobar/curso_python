# Solicitamos el primer número
print('Buen día! Ingrese el primer número:', end=' ****> ')
primera_cadena = input()

print('\n\n', primera_cadena, type(primera_cadena))

primer_numero = int(primera_cadena)  # Cambiamos el tipo de datos de cadena de caracteres (str) a número entero (int)
print(primer_numero, type(primer_numero))


# Solicitamos el segundo número
print('Ahora, por favor, ingrese el segundo número:', end=" ")
segunda_cadena = input()
segundo_numero = int(segunda_cadena)

# Calculamos el resultado
resultado = primer_numero + segundo_numero

# Mostramos el resultado
print('La suma de ambos números es igual a:', resultado)
