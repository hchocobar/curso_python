# métodos de cadenas
# La lista completa de métodos se presenta aquí:
# https://docs.python.org/3.4/library/stdtypes.html#string-methods

# Ejemplos
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
dígitos = "0123456789"
traba_lengua = 'rueda rueda la rueda del Ferrocarril'
digitos_trab = '012345678901234567890123456789012345'
pregunta = "¿Dónde está la gente?"

# método.index - busca en la secuencia desde el principio para encontrar el 1er elemento que coincide con su argumento
print(alfabeto.index("i"))
# print(alfabeto.index("ijk"))
# print(alfabeto.index("Z"))
# print(traba_lengua.index('del'))
# 
# # otros métodos
print(traba_lengua.count('rueda'))
print(traba_lengua.capitalize())
print(traba_lengua.lower())
print(alfabeto.upper())
print(traba_lengua.center(120, ' '))
# 
# # Demostración del método endswith()
print(alfabeto.endswith("xyz"))
#
# # Demostración del método startswith()
print(alfabeto.startswith("abc"))
#
lista_palabras = traba_lengua.split(' ')
print(type(lista_palabras))
print(len(lista_palabras))
print(lista_palabras)
print(lista_palabras[5])

email = 'hector@gmail.com'
list_email = email.split('@')
print(list_email)
# input()
# # Demostración del método find()
# print(traba_lengua.find("Ferrocarril"))  # devuelve el nro del indice donde inicia la cadena
# print(traba_lengua.find("avión"))  # devuelve -1 (no devuelve error)
#
# # Demostración del método the isalnum() - es alfanumérico
# print(alfabeto.isalnum(), end=" ")
# print(dígitos.isalnum(), end=" ")
# print(traba_lengua.isalnum(), end=" ")
# print(pregunta.isalnum())
# #
# # Demostración del método isalpha()
# print(alfabeto.isalpha(), end=" ")
# print(dígitos.isalpha())
#
# # Demostración del método isdigit()
# print(alfabeto.isdigit(), end=" ")
# print(dígitos.isdigit())

# Demostración del método join()
# une las cadenas del argumento insertando la cadena que lo invoca entre cada cadena del argumento
# el argumento debe ser una lista de cadenas (sino da error)
# print(",".join(["alpha", "beta", "delta", "gama"]))
#
# cadena1 = " letra griega.\n"
# print(cadena1.join(["alpha", "beta", "delta", "gama", ""]))

# # Demostración del método the lstrip()
# print("  Elimino espacios iniciales".lstrip())
# print("www.chocobar.net".lstrip("w."))

# # Demostración del método replace()
# print("This is it!".replace("is", "are"))

# # Demostración del método rfind() - reverse find
# str.rfind((sub[, start[, end]])
# print(traba_lengua)
# print(digitos_trab)
# print(traba_lengua.rfind("rueda"), end=" ")
# print(traba_lengua.rfind("rueda", 5), end=" ")
# print(traba_lengua.rfind("rueda", 1, 15), end=" ")
# print(traba_lengua.rfind("rueda", 1, 10))
#
# suma = 1 + 2
# producto = 1 * 2
# print("The sum of 1 + 2 is {} y el producto es {}".format(suma, producto))
# # 'The sum of 1 + 2 is 3'
# name = 'Hector'
# last_name = 'Chocobar'
# print('nombre: {}, Apellido: {}'.format(name, last_name))
# print('nombre: {}, Apellido: {}')
