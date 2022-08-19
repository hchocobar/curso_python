""" El protocolo iterador es una forma en que un objeto debe comportarse para ajustarse a las reglas impuestas por el
contexto de las sentencias for e in. Un objeto conforme al protocolo iterador se llama iterador.

Un iterador debe proporcionar dos métodos:

__iter__() devuelve el objeto en sí y se invoca una vez (es necesario para que Python inicie con éxito la iteración).

__next__() devuelve el siguiente valor de la serie deseada: será invocado por las sentencias for/in para pasar a la
siguiente iteración; si no hay más valores a proporcionar, el método deberá lanzar la excepción StopIteration. """

""" Serie Fibonacci 
Los primeros dos números son 1.
Cualquier otro número de Fibonacci es la suma de los dos anteriores y así sucesivamente."""


class Fibonacci:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fibonacci(10):
    print(i)
