import math

x = float(input("Ingrese x: "))  # fallará si ingresamos una cadena
y = math.sqrt(x)  # fallará si ingresamos un valor negativo

print("La raíz cuadrada de", x, "es:", y)
