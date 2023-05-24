# Implementación de una Pila mediante una clase
class Pila:
    def __init__(self):  # Constructor de la clase
        self.__lista_pila = []  # Definimos una variable privada (pseudo-encapsulamos)

    def push(self, val):  # El parámetro self apunta a la clase misma, Python lo agregará siempre como primer argumento
        self.__lista_pila.append(val)

    def pop(self):
        val = self.__lista_pila[-1]
        del self.__lista_pila[-1]
        return val


'''Nota: Faltaría implementar un try/except para evitar el error que ocasionaría un pop() en una pila vacía'''
objeto_pila = Pila()

objeto_pila.push(3)  # El argumento self no se envía, Python lo agregará siempre
objeto_pila.push(2)
objeto_pila.push(1)

print(objeto_pila.pop())
print(objeto_pila.pop())
print(objeto_pila.pop())
