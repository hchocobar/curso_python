# Ejemplo de sentencia condicional 'if'
numero = int(input('Por favor, ingresa un número: '))  # Solicitamos un número
if numero == 100:
    print("ingresó", numero)  # Verdadero
elif numero > 100:  # Falso, otra pregunta  else if
    print('Muestra 2')
    print(numero * 20)
elif numero < 300:
    print('Muestra 3')
    print(numero * 30)
else:  # Falso
    print('Muestra 4')
    print(numero * 40)

if 1000 < numero < 2000:
    pass  # No ejecuta nada, pero es una palabra clave de python
