""" Custom Exception
Podemos definir nuestras propias excepciones como subclases derivadas de las predefinidas."""


class PizzaError(Exception):
    def __init__(self, pizza='Desconocida', mensaje=''):
        Exception.__init__(self, mensaje)
        self.pizza = pizza


class DemasiadoQuesoError(PizzaError):
    def __init__(self, pizza='Desconocida', queso='>100', mensaje=''):
        PizzaError.__init__(self, pizza, mensaje)
        self.queso = queso


def make_pizza(pizza, queso):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no hay tal pizza en el menú")
    if queso > 100:
        raise DemasiadoQuesoError(pizza, queso, "demasiado queso")
    print("¡Pizza lista!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except DemasiadoQuesoError as dqe:
        print(dqe, ':', dqe.queso)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
