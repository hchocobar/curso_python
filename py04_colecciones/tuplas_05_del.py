# Las tuplas son inmutables
# Sin embargo, se puede eliminar:
miTupla = 1, 2, 3,
print(miTupla)

del miTupla
print(miTupla)  # NameError: name 'miTupla' is not defined
