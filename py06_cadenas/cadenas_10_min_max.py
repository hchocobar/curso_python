# min() - devuelve el caracter de menor valor ASCII-UNICODE de la cadena
print(min("aAbByYzZ"))  # Salida: A
print(ord(min("aAbByYzZ")))  # Salida: 65

t = '¡Los Caballeros Que Dicen!'
print('[' + min(t) + ']')  # Salida: [ ]  Devuelve un espacio en blanco cuyo valor es 32

# max() - devuelve el caracter de mayor valor ASCII-UNICODE de la cadena
print(max("aAbByYzZ"))  # Salida: z

print('[' + max(t) + ']')  # Salida: [¡]
