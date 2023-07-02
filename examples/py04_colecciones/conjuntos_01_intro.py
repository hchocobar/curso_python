# Creación de conjunto mediante {}
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # Salida: {'orange', 'banana', 'pear', 'apple'}
print('orange' in basket)  # Salida: True
print('crabgrass' in basket)  # Salida: False

# Creación de conjunto mediante set()
set_a = set()  # Crea un conjunto vacío
print(set_a)
print(type(set_a))

# Comparación de la creación de conjuntos desde una palabra
set_m = set('abracadabra')  # Crea un conjunto con todas las letras únicas de la palabra
set_n = {'abracadabra'}  # Crea un conjunto con un solo elemento
print(set_m)
print(set_n)
print(type(set_m), type(set_n))

# La función integrada set() recibe un solo argumento
basket_set = set(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])
print(basket_set)
