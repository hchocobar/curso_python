# Slicing operator
# Vea también cadenas_07_rodajas.py
# Sintaxis: list[position_start:position_end_less_one]

# Copiando toda la lista
lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)  # Salida: [1]

# Copiando parte de la lista
mi_lista = [10, 8, 6, 4, 2]
nueva_lista = mi_lista[1:3]
print(nueva_lista)  # Salida: [8, 6]

lista = mi_lista[::-1]
print(lista)  # Salida: [2, 4, 6, 8, 10]
