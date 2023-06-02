# La jerarquía de un error de división por cero es la siguiente:
# BaseException / Exception / ArithmeticError / ZeroDivisionError
try:
    foo = 1 / 0
except ZeroDivisionError:
    print("Ups... división por cero")

print("Fin ejemplo 1")

try:
    foo = 1 / 0
except ArithmeticError:
    print("Ups... error aritmético")

print("Fin ejemplo 2")

try:
    foo = 1 / 0
except Exception:
    print("Ups... excepción")

print("Fin ejemplo 3")

try:
    foo = 1 / 0
except BaseException:  # Es la excepción más general, por lo tanto, esta instrucción es igual a except:
    print("Ups... excepción base")

print("Fin ejemplo 4")
