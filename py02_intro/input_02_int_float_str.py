# input siempre nos devuelve una cadena
# para introducir un número entero utilice int() y
# para un número decimal utilice float()
# para convertir un número en cadena utilice str()

cadena = input('Introduce una cadena de texto: ')
print('La cadena de texto que ingreso es: ', cadena)

# para introducir un número entero utilizamos int() y
numero_entero = int(input('Introduce un numero entero: '))
print('El numero entero que ingreso es: ', numero_entero)

# para introducir un número decimal utilizamos float()
numero_decimal = float(input('Introduce un numero decimal: '))
print('El numero decimal que ingreso es: ', numero_decimal)

# para convertir un número en cadena utilizamos str()
nueva_cadena = str(numero_decimal)
print("El número convertido en cadena es:", nueva_cadena)
