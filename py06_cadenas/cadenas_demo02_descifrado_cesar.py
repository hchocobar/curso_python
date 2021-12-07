# El cifrado César: descifrando un mensaje
#
# La operación inversa ahora debería ser clara para ti
#
# Observa el código en el editor. Comprueba cuidadosamente si funciona. Usa el criptograma del programa anterior.
cifrado = input('Ingresa tu criptograma: ')
text = ''
for char in cifrado:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)
