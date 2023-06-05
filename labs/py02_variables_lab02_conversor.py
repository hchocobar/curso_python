km = 12.25
millas = 7.38

millas_a_km = millas * 1.61
km_a_millas = km / 1.61

# La función integrada round() nos devuelve el redondeo de un número con determinada cantidad de decimales
print(millas, " millas son ", round(millas_a_km, 2), " kilómetros ")
print(km, " kilómetros son ", round(km_a_millas, 2), " millas ")
