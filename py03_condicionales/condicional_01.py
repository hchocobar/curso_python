numero = int(input('Por favor, ingresa un número: '))
if numero == 100:
    print("ingreso")
elif numero > 100:
    print('Muestra 2')
    print(numero * 20)
elif not (numero < 300):
    print('Muestra 3')
    print(numero * 30)
else:
    print('Muestra 4')
    print(numero * 40)
if 1000 < numero < 2000:
    pass
