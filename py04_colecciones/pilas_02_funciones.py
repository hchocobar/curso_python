# Implementación de las operaciones push y pop mediante funciones
def push(val):
    pila.append(val)


def pop():
    val = pila[-1]
    del pila[-1]
    return val


'''Importante: Esta implementación no protege los datos de nuestra lista. Por ejemplo dentro del código se podría 
ejecutar un insert() y con esto no estaríamos cumpliendo los requisitos de las pilas '''
pila = []

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
