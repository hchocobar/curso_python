# Creación de conjunto mediante {}
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # salida: {'orange', 'banana', 'pear', 'apple'}
print('orange' in basket)  # salida: True
print('crabgrass' in basket)  # salida: False


# creación de conjunto mediante set()
a = set()  # crea un conjunto vacío
print(a)
print(type(a))


# comparación de creación de conjunto desde una palabra
m = set('abracadabra')  # crea un conjunto con todas las letras únicas de la palabra
n = {'abracadabra'}  # crea un conjunto con un solo elemento
print(m)
print(n)
print(type(m), type(n))

# set() recibe un solo argumento
basket_set = set(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])
print(basket_set)
