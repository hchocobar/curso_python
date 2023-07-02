# Ordenamos una lista numérica ingresada desde consola
mi_lista = []
intercambiado = True
cantidad = int(input("¿Cuántos elementos deseas ordenar?:"))

for i in range(cantidad):
    valor = float(input("Introduce un elemento de la lista:"))
    mi_lista.append(valor)

while intercambiado:
    intercambiado = False
    for i in range(len(mi_lista) - 1):
        if mi_lista[i] > mi_lista[i + 1]:
            intercambiado = True
            mi_lista[i], mi_lista[i + 1] = mi_lista[i + 1], mi_lista[i]
        print(mi_lista)
    print()

print("\nOrdenado:")
print(mi_lista)
