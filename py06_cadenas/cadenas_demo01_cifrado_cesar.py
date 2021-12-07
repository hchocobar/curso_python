# El Cifrado César: encriptando un mensaje
#
# Este cifrado fue (probablemente) inventado y utilizado por Cayo Julio César y sus tropas durante las Guerras Galas.
# La idea es bastante simple: cada letra del mensaje se reemplaza por su consecuente más cercano (A se convierte en
# B, B se convierte en C, y así sucesivamente). La única excepción es Z, la cual se convierte en A.
#
# El programa en el editor es una implementación muy simple (pero funcional) del algoritmo.
#
# Se ha escrito utilizando los siguientes supuestos:
#
# Solo acepta letras latinas (nota: los romanos no usaban espacios en blanco ni dígitos).
# Todas las letras del mensaje están en mayúsculas (nota: los romanos solo conocían las mayúsculas).
# Veamos el código:

# Cifrado César
text = input("Ingresa tu mensaje: ")  # solicita un mensaje
cifrado = ''  # cadena vacía para guardar el mensaje cifrado
for char in text:  # inicia la iteración a través del mensaje.
    if not char.isalpha():  # si el caracter actual no es alfabético...
        continue  # ...ignoralo.
    char = char.upper()  # convierte la letra a mayúsculas
    code = ord(char) + 1  # obtiene el código de la letra y lo incrementa
    if code > ord('Z'):  # si el código resultante ha "dejado" el alfabeto latino (si es mayor que el código de la Z)...
        code = ord('A')  # ... cámbialo al código de la A
    cifrado += chr(code)  # agrega el carácter recibido al final del mensaje cifrado

print(cifrado)  # imprime el cifrado.

# Dato de prueba
# AVE CAESAR salida: BWFDBFTBS
