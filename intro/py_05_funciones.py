"""
Funciones
 - def 
 - Indentación y bloques
   - pass
 - argumentos, parámetros
   - argumentos posicionales
   - argumentos por palabra clave
   - mix de argumentos posicionales y palabras clave
   - parámetros con valores por defecto
 - Return / None
 - Alcance (scope) / global / cuidado: sombra
"""


def saludo(name, greeting='Buen día'):
    """ 1. Declaro la función """
    # print(greeting, name)
    # return greeting + ', ' + name + '!'
    return f'{greeting}, {name}!'


# Invoco o ejecuto mi función
text = saludo('Susana')
print(text)
