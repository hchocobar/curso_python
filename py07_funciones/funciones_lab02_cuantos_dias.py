# LABORATORIO 4.1.3.7
#
# Tiempo estimado
# 15-20 minutos
#
# Nivel de dificultad
# Medio
#
# Requisitos previos
# LABORATORIO 4.1.3.6
#
# Objetivos
# Familiarizar al estudiante con:
# - Proyectar y escribir funciones parametrizadas.
# - Utilizar la sentencia return.
# - Utilizar las funciones propias del estudiante.
#
# Escenario
#
Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días
del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).

La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen
sentido.

Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LAB 01). Puede ser muy útil.
Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de la función; este truco acortará
significativamente el código.

Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.

def isYearLeap(year):
#
# tu código del LAB 01 de funciones
#

def daysInMonth(year, month):
#
# coloca tu código aquí
#

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
