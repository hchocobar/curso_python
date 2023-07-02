# Las cadenas de Python son secuencias inmutables.

# Ejemplo 1
palabra = 'palabra'
print(len(palabra))  # Salida: 7

# Ejemplo 2
palabra_vacia = ''
print(len(palabra_vacia))  # Salida: 0

# Ejemplo 3
yo_soy = 'I\'m'
print(len(yo_soy))  # Salida: 3 - la diagonal invertida (\ escape), no cuenta para la longitud total de la cadena

# Ejemplo 4
multiLinea = '''Línea 1
Linea 2'''
print(len(multiLinea))  # Salida: 15 - recuerda el \n

# Ejemplo 5
multiLinea = 'Línea 1\nLinea 2'
print(len(multiLinea))  # Salida: 15 - recuerda el \n
