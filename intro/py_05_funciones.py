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


# def saludo(name, greeting='Buen día'):
#     """ 1. Declaro la función """
#     # print(greeting, name)
#     # return greeting + ', ' + name + '!'
#     return f'{greeting}, {name}!'

def saludo(name, last_name='Doe', prefix='Buen día'):
    """
    last_update: 27/10/2016 - version: 1.1
    :param name: Recibe un string válido, corresponde al nombre de una persona
    :return: un saludo
    """
    greeting = f'{prefix} {name} {last_name}'
    if name == '':
        return 'Hola Mundo'
    return greeting

# Invoco o ejecuto mi función
nombre = input('escribe tu nombre: ')
apellido = input('ingres su apellido: ')
text = saludo(nombre, prefix='Buenas tardes')
print(text)
