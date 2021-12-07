miLista = [5, 10, 7]  # quiero mostrar [10, 5, 7]

auxiliar = miLista[0]
miLista[0] = miLista[1]
miLista[1] = auxiliar
print(miLista)

# En Python disponemos de lo siguiente que facilita esta asignación
miLista = [5, 10, 7]
miLista[0], miLista[1] = miLista[1], miLista[0]
print(miLista)
