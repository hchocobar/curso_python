"""Comencemos desde la raíz del árbol:
La raíz de las clases de excepciones de Python es la clase BaseException (superclase de todas las demás excepciones).

Para cada una de las clases encontradas, se realiza el mismo conjunto de operaciones:

- Imprimir su nombre, tomado de la propiedad __name__.
- Iterar a través de la lista de subclases provistas por el método __subclasses__(),
- e invocar recursivamente la función print_exception_tree(), incrementando el nivel de anidación respectivamente. """


def print_exception_tree(this_class, nest=0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")
    print(this_class.__name__)
    for subclass in this_class.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)
