# solicitamos el primer número
print('Buen día! Ingrese el primer número:', end=" ")
primera_cadena = input()
primer_numero = int(primera_cadena)  # cambiamos el tipo de datos de cadena de caracteres (str) a número entero (int)

# solicitamos el segundo número
print('Ahora, por favor, ingrese el segundo número:', end=" ")
segunda_cadena = input()
segundo_numero = int(segunda_cadena)
resultado = primer_numero + segundo_numero

# mostramos el resultado
print('La suma de ambos números es igual a:', resultado)
