# El Procesador de Números
linea = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = linea.split()  # Divide la línea en una lista con subcadenas.
total = 0  # Se inicializa la suma total a cero.

# Como la conversión de cadena a flotante puede generar una excepción, utilizamos la protección del bloque try-except
try:
    for substr in strings:  # Itera a través de la lista...
        total += float(substr)  # Convierte todos sus elementos en números flotantes; si funciona, aumenta la suma.
    print("El total es:", total)  # Imprime la suma
except:  # El programa termina aquí en caso de error
    print(substr, "no es un numero.")  # Imprime un mensaje de diagnóstico que muestra al usuario el motivo del error.
