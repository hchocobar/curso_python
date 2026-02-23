# hora = int(input("Hora de inicio (horas): "))
# minuto = int(input("Minuto de inicio (minutos): "))
# duracion = int(input("Duración del evento (minutos): "))
# print(hora, minuto, duracion )


# 1. Si la suma minutos es inferior a 59 minutos,
#    1.1. esto es simple, solo sumo los minutos
#    1.2. Si la suma minutos es superior a 59 minutos, se debe calcular la suma de horas
# 2. Si la suma de horas supera las 23 horas, se debe calcular la suma de horas

#
# calculo_minutos = minuto + duracion
# calculo_hora = hora
# minutos_final = calculo_minutos
# if calculo_minutos >= 60:
#     minutos_final = calculo_minutos % 60
#     calculo_hora = hora + calculo_minutosresultado_minutos // 60

# print(calculo_hora, ':' , minutos_final)



# Lee tres números
numero_1 = int(input("Ingresa el primer número:"))
numero_2 = int(input("Ingresa el segundo número:"))
numero_3 = int(input("Ingresa el tercer número:"))

# Asumimos temporalmente que el primer número es el más grande
mas_grande = numero_1

# Comprobamos si el segundo número es más grande que el mayor número actual
if numero_2 > mas_grande:
    mas_grande = numero_2  # Actualizamos el número más grande si es necesario

# Comprobamos si el tercer número es más grande que el mayor número actual
if numero_3 > mas_grande:
    mas_grande = numero_3  # Actualizamos el número más grande si es necesario

# Imprimimos el resultado
print("El número más grande es:", mas_grande)