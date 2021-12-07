# break - ejemplo

print("La instrucción de ruptura:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continua - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 4:
        break
    if i == 2:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")
