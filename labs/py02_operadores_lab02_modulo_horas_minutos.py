# Calcula el horario de finalización de un evento
hora_inicio = int(input("Hora de inicio (horas): "))
minuto_inicio = int(input("Minuto de inicio (minutos): "))
duracion_del_evento = int(input("Duración del evento (minutos): "))

# Coloca tu código aquí
horas_adicionales = (minuto_inicio + duracion_del_evento) // 60
hora_fin = (hora_inicio + horas_adicionales) % 24

minutos_fin = (minuto_inicio + duracion_del_evento) % 60

print(hora_fin, ":", minutos_fin, sep='')

"""
Datos de Prueba:

Hora de inicio: 23
Minuto de inicio: 15
Duración del evento: 70 

Salida esperada: 0:25
"""