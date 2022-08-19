# Solicitamos el primer número
print('Buen día! Ingrese el número a: ', end=" ")
a = input()
a = int(a)  # cambiamos el tipo de datos de cadena de caracteres (str) a número entero (int)

# Solicitamos el segundo número
print('Ahora ingresá el número b: ')
b = input()
b = int(b)
c = a + b

# Mostramos el resultado
print('La suma de ambos es igual a ', c)
