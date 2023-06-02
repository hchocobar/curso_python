""" Propiedad args

La clase BaseException introduce una propiedad llamada args que es una tupla diseñada para reunir todos los
argumentos pasados al constructor de la clase.

- Esta tupla está vacía si la construcción se ha invocado sin ningún argumento.
- Contiene un elemento cuando el constructor recibe un argumento (no se considera el argumento self aquí).
- Y contiene más, si se enviaron más argumentos."""


def print_args(args):
    cantidad_de_argumentos = len(args)
    if cantidad_de_argumentos == 0:
        print("")
    elif cantidad_de_argumentos == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' - ')
    print_args(e.args)

try:
    raise Exception("1er argumento")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' - ')
    print_args(e.args)

try:
    raise Exception("1er argumento", "2do argumento")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' - ')
    print_args(e.args)
