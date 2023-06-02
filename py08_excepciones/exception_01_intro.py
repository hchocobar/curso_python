import math as m

foo = float(input("Ingrese un número: "))  # Fallará si ingresamos una cadena
bar = m.sqrt(foo)  # Fallará si ingresamos un valor negativo

print("La raíz cuadrada de", foo, "es:", bar)
