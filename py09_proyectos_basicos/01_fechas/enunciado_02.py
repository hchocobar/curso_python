# Laboratorio 2
# Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días
# del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).
# La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.
# Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (Laboratorio 1). Puede ser muy útil.
# Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de la función; este truco acortará
# significativamente el código.
# Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.
def is_year_leap(year):
    #
    # tu código del LAB 01 de funciones
    #

def days_in_month(year, month):
    #
    # coloca tu código aquí
    #

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Error")


