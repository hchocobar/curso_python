# Slicing operator
# Rodajas, rebanadas, slicing
# cadena[position_start:position_end_less_one:step]
cadena = "01234567890"
#           987654321
# cadena = "012345678901234567890"
#
print(cadena)
print(cadena[1:3])
# print(cadena[1:3:1])
# print(cadena[3:])
# print(cadena[:3])
# print(cadena[3:-2])  # cadena[3:9]
# print(cadena[-3:4], 'algo')  # cadena[8:4]
# print(cadena[-10:8], 'otro algo')  # cadena[10:8]
# print(cadena[::2])  # saltando cada 2 elementos
# print(cadena[1::2])
# print(cadena[1:8:2])
#
# # indice negativo -> recorre la cadena desde el fin hacia el inicio
# print()
print(cadena[-1:-10:-2])
print(cadena[::-1])
#
