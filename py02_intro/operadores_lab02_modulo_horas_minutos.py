hora = int(input("Hora de inicio (horas): "))
minuto = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aquí
horas_adicionales = (minuto + dura) // 60
hora_fin = (hora + horas_adicionales) % 24

minutos_fin = (minuto + dura) % 60

print(hora_fin, ":", minutos_fin)
