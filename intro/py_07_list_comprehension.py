"""
List Comprehension:
https://gist.github.com/hchocobar/d12d31c4ccde8a5f6c318d3eb02f7789

Dict Comprehension:
nueva_lista = [target for item in lista_anterior]
nueva_lista = [target for item in <lista_anterior> if <condición>]

Condicional one liner:
valor = verdadero if condition else falso
"""
students = ['Agustin', 'Alejandro', 'Anais', 'Pau', 'Pablo', 'David', 'Mary', 'Bilbo',
            'Matias', 'Marco', 'Mar', 'Victoria', 'Gabriela', 'Fidel', 'Robert', 'Eduardo']
numbers = [10, 23, 8, 65, 34, 18, 22, 88, 70]

# Creo nueva lista
saludo = ['Hola ' + item for item in students]
print(saludo)


# Creo nueva lista con un condicional
# pares = [item for item in numbers if item % 2 == 0]
# print(pares)

# Valido a través de una condición.
is_login = True
text = 'User logged' if is_login else 'No hay usuario'
print(text)
