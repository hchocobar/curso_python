# Listas - 02 - Recorriendo las listas
# for in range/len
# for in my_lista
mi_lista = [10, 1, 8, 3, 5]
suma = 0

for i in range(len(mi_lista)):
    suma += mi_lista[i]
print(suma)

suma = 0
for i in mi_lista:
    suma += i
print(suma)

mi_lista = [10, 1, 8, 3, 5]
longitud = len(mi_lista)

for i in range(longitud // 2):
    mi_lista[i], mi_lista[longitud - i - 1] = mi_lista[longitud - i - 1], mi_lista[i]
print(mi_lista)
