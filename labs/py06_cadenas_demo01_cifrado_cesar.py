# Cifrado César
text = input("Ingresa tu mensaje: ")  # Solicita un mensaje
cifrado = ''  # Cadena vacía para guardar el mensaje cifrado
for char in text:  # Inicia la iteración a través del mensaje.
    if not char.isalpha():  # Si el caracter actual no es alfabético...
        continue  # Ignoralo.
    char = char.upper()  # Convierte la letra a mayúsculas
    code = ord(char) + 1  # Obtiene el código de la letra y lo incrementa
    if code > ord('Z'):  # Si el código resultante ha "dejado" el alfabeto latino (si es mayor que el código de la Z)...
        code = ord('A')  # Cámbialo al código de la A
    cifrado += chr(code)  # Agrega el carácter recibido al final del mensaje cifrado

print(cifrado)  # Imprime el cifrado.
