# Ejemplo de sentencia condicional if
numero = int(input('Por favor, ingresa un número: '))  # solicitamos un número
if numero == 100:
    print("ingresó", numero)  # verdadero
elif numero > 100:  # falso, otra pregunta  else if
    print('Muestra 2')
    print(numero * 20)
elif numero < 300:
    print('Muestra 3')
    print(numero * 30)
else:  # falso
    print('Muestra 4')
    print(numero * 40)

if 1000 < numero < 2000:
    pass  # no ejecuta nada, pero es una key de python
