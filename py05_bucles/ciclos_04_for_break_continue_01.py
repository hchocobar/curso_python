# break - ejemplo

# print("La instrucción de ruptura:")
# for i in range(6):
#     print("Dentro del ciclo - antes del break", i)
#     if i == 3:
#         break
#     print("Dentro del ciclo - después del break", i)
# print("Fuera del ciclo.")

# continua - ejemplo
print("\nLa instrucción continue:")
for i in range(1, 6):
    print()
    print("Dentro del ciclo - antes del break", i)
    if i == 4:
        break
    print("Dentro del ciclo - después break", i)
    if i == 2:
        continue
    print("Dentro del ciclo - después continue.", i)
print("Fuera del ciclo.")
