# LABORATORIO 4.1.3.10
#
# Tiempo estimado
# 10-15 minutos
#
# Nivel de dificultad
# Fácil
#
# Objetivos
# Mejorar las habilidades del estudiante para definir, utilizar y probar funciones.
#
# Escenario
#
# El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes. Por ejemplo, en Europa,
# se muestra como la cantidad de combustible consumido por cada 100 kilómetros.
#
# En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón de combustible.
#
# Tu tarea es escribir un par de funciones que conviertan l/100km a mpg(millas por galón), y viceversa.
#
# Las funciones:
#
# Se llaman l100kmampg y mpgal100km respectivamente.
# Toman un argumento (el valor correspondiente a sus nombres).
# Complementa el código en el editor.
#
# Ejecuta tu código y verifica si tu salida es la misma que la nuestra.
#
# Aquí hay información para ayudarte:
# # 1 milla = 1609.344 metros.
# 1 galón = 3.785411784 litros.
#
# Datos de prueba
# Salida esperada:
#
# 60.31143162393162
# 31.36194444444444
# 23.52145833333333
# 3.9007393587617467
# 7.490910297239916
# 10.009131205673757
#
#
def l100km_to_mpg(liters):
    mpg = (100 / millas_km) / (liters / galones_lts) * 1000
    return mpg

def mpg_to_l100km(miles):
    return (100 * galones_lts) / (miles * millas_km) * 1000
    pass

millas_km = 1609.344
galones_lts = 3.785411784

print(l100km_to_mpg(3.9))
print(l100km_to_mpg(7.5))
print(l100km_to_mpg(10.))
print(mpg_to_l100km(60.3))
print(mpg_to_l100km(31.4))
print(mpg_to_l100km(23.5))