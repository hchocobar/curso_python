mi_lista = ["blanco", "purpura", "azul", "amarillo", "verde"]

for color in mi_lista:
    print(color)

print(len(mi_lista))  # Salida: 5

del mi_lista[2]
print(len(mi_lista))  # Salida: 4
print(mi_lista[len(mi_lista)-1])  # Salida: verde
