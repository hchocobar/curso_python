# Laboratorio
año = int(input("Introduzca un año: "))
# Coloca tu código aquí.
if año % 4 != 0:
    print("Año común")
elif año % 100 != 0:
    print("Año bisiesto")
elif año % 400 != 0:
    print("Año común")
else:
    print("Año bisiesto")
