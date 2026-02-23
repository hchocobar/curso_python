calificacion = int(input("Ingrese su calificacion entre 0 y 6: "))
asistencia = float(input("Ingrese su porcentaje de asistencia: "))  # menor 70% no aprueba

if calificacion == 0:
    print("No puedes pasar")
elif calificacion < 3:
    print("Debe revisar")
elif asistencia < 0.7:
    print("No cumples con la asistencia mínima, por lo tanto no puede pasar")
elif calificacion == 3:
    print("Puede pasar")
elif calificacion <= 4:
    print("Puede pasar con aviso")
elif calificacion <= 5:
    print("Muy buen desempeño")
else:
    print("Felicitaciones")
