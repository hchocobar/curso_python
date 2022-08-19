# Implementación de una pila utilizando listas
stack = [3, 4, 5]
print(stack)  # salida: [3, 4, 5]
print(type(stack))

# apilamos (agregamos) elementos utilizando .append()
stack.append(6)
stack.append(7)
print(stack)  # salida: [3, 4, 5, 6, 7]


# des-apilamos (sacamos) elementos utilizando .pop()
stack.pop()  # elimina el último elemento 7
print(stack)  # salida: [3, 4, 5, 6]
stack.pop()
print(stack)  # salida: [3, 4, 5]
stack.pop()
print(stack)  # salida: [3, 4]


'''Importante: Esta implementación no protege los datos de nuestra lista. Por ejemplo dentro del código se podría 
ejecutar un insert() y con esto no estaríamos cumpliendo los requisitos de las pilas '''