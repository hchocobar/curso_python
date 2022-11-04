# Laboratorio
ingreso = float(input("Ingrese el ingreso anual: "))
minima = 85528
exencion_fiscal = 556.02

if ingreso <= minima:
    impuesto = (ingreso * 0.18) - exencion_fiscal
else:
    impuesto = 14839.02 + (ingreso - minima) * 0.32
if impuesto < 0:
    impuesto = 0

impuesto = round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")
