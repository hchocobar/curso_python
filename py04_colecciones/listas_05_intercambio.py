# Intercambiar elementos dentro de una lista
mi_lista = [5, 10, 7]  # Deseo mostrar [10, 5, 7]

# La forma estándar, utilizando un variable auxiliar para intercambiar elementos en una lista
auxiliar = mi_lista[0]
mi_lista[0] = mi_lista[1]
mi_lista[1] = auxiliar
print(mi_lista)  # Salida [10, 5, 7]

# En Python disponemos de lo siguiente que facilita esta asignación
mi_lista = [5, 10, 7]
mi_lista[0], mi_lista[1] = mi_lista[1], mi_lista[0]
print(mi_lista)  # Salida [10, 5, 7]
