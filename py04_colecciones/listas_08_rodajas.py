# Slicing operator
# ver también cadenas_07_rodajas.py
# list[position_start:position_end_less_one]

# Copiando toda la lista
lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)  # [1]

# Copiando parte de la lista
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:3]
print(nuevaLista)  # [8, 6]
