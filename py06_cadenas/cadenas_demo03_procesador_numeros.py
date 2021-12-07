# El Procesador de Números
#
# Este programa muestra un método simple que permite ingresar una línea llena de números y sumarlos fácilmente.
#
# Nota: la función input(), combinada junto con las funciones int() o float(), no es lo adecuado para este propósito.
#
# El procesamiento será extremadamente fácil: queremos que se sumen los números.
#
# Observa el código en el editor. Analicémoslo.
#
# Emplear listas puede hacer que el código sea más pequeño. Puedes hacerlo si quieres.
#
# pide al usuario que ingrese una línea llena de cualquier cantidad de números (los números pueden ser flotantes).
linea = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = linea.split()  # divide la línea en una lista con subcadenas.
total = 0  # se inicializa la suma total a cero.
# como la conversión de cadena a flotante puede generar una excepción, utilizamos la protección del bloque try-except
try:
    for substr in strings:  # itera a través de la lista...
        total += float(substr)  # intenta convertir todos sus elementos en números flotantes; si funciona, aumenta la suma.
    print("El total es:", total)  # imprime la suma
except:  # el programa termina aquí en caso de error
    print(substr, "no es un numero.")  # imprime un mensaje de diagnóstico que muestra al usuario el motivo del error.

# El código tiene una debilidad importante:
# muestra un resultado falso cuando el usuario ingresa una línea vacía. ¿Puedes arreglarlo?


