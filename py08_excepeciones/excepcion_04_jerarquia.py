# La jerarquía de un error de división por cero es la siguiente:
# BaseException / Exception / ArithmeticError / ZeroDivisionError
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Ups... división por cero")

print("Fin ejemplo 1")

try:
    y = 1 / 0
except ArithmeticError:
    print("Ups... error aritmético")

print("Fin ejemplo 2")

try:
    y = 1 / 0
except Exception:
    print("Ups... excepción")

print("Fin ejemplo 3")

try:
    y = 1 / 0
except BaseException:  # es la excepción mas general, por lo tanto esta instrucción es igual a except:
    print("Ups... excepción base")

print("Fin ejemplo 4")
