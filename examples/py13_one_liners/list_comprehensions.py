"""
Reference
https://gist.github.com/hchocobar/d12d31c4ccde8a5f6c318d3eb02f7789


List Comprehension, Syntax:
nueva_lista = [target for item in lista_anterior]
nueva_lista = [target for item in lista_anterior if condición]

Condicional one liner, Syntax:
valor = verdadero if condición else falso
"""
friends = ['Gonzalo', 'Nicolás', 'Alejandra', 'Martín', 'Miguel', 'Victoria',
           'Javier', 'Alicia', 'Gabriela', 'Carolina', 'Lionel', 'Leticia']
greetings = [f'Hola {item}! Como estás?' for item in friends]
print(greetings)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds = [number for number in numbers if number % 2 == 1]
print(odds)
evens = [number for number in numbers if number % 2 == 0]
print(evens)

# Conditional one liner
condition = True
print('Verdadero' if condition else 'Falso')
