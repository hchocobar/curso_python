# LABORATORIO 4.1.3.6
#
# Tiempo estimado
# 10-15 minutos
#
# Nivel de dificultad
# Fácil
#
# Objetivos
# Familiarizar al estudiante con:
#  - Proyectar y escribir funciones con parámetros.
#  - Utilizar la sentencia return.
#  - Probar las funciones.
#
Escenario

Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año
bisiesto, o False sí no lo es.

Parte del esqueleto de la función ya está en el editor.

Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.

El código utiliza dos listas: una con los datos de prueba y la otra con los resultados esperados. El código te dirá
si alguno de tus resultados no es válido.
def isYearLeap(year):
#
# coloca tu código aquí
#

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
