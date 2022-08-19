# Implementación de una Pila mediante una clase
class Pila:
    def __init__(self):  # constructor de la clase
        self.__lista_pila = []  # definimos una variable privada (pseudo-encapsulamos)

    def push(self, val):  # el parámetro self apunta a la clase misma, Python lo agregará siempre como primer argumento
        self.__lista_pila.append(val)

    def pop(self):
        val = self.__lista_pila[-1]
        del self.__lista_pila[-1]
        return val


objeto_pila = Pila()

objeto_pila.push(3)  # el argumento self no se envía, Python lo agregará siempre
objeto_pila.push(2)
objeto_pila.push(1)

print(objeto_pila.pop())
print(objeto_pila.pop())
print(objeto_pila.pop())

'''Nota: Faltaría implementar un try/except para evitar el error que ocasionaría un pop() en una pila vacía'''
