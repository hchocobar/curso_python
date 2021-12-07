# Laboratorio 1
# Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False sí no lo es.
# Desde la introducción del calendario gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:
# - Si el número del año no es divisible entre cuatro, es un año común.
# - De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
# - De lo contrario, si el número del año no es divisible entre 400, es un año común.
# - De lo contrario, es un año bisiesto.
#
# Parte del esqueleto de la función ya está en el editor.
# Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.
# El código utiliza dos listas:
#     • una con los datos de prueba y
#     • la otra con los resultados esperados.
# El código te dirá si alguno de tus resultados no es válido.
def is_year_leap(year):
#
# coloca tu código aquí
#

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Error")

