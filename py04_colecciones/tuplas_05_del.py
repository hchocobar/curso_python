# Las tuplas son inmutables
# Sin embargo, se puede eliminar:
mi_tupla = 1, 2, 3,
print(mi_tupla)  # Salida: (1, 2, 3)

del mi_tupla
print(mi_tupla)  # NameError: name 'mi_tupla' is not defined
