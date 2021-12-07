# La tupla de un solo elemento se define de la siguiente manera:
miTupla1 = ("uno",)  # paréntesis y coma
miTupla2 = "uno",  # sin paréntesis, solo la coma
print(miTupla1)
print(miTupla2)

# Si se elimina la coma, Python creará una variable no una tupla:
miTup1 = 1,
print(type(miTup1))  # salida: <class 'tuple'>
miTup2 = 1
print(type(miTup2))  # salida: <class 'int'>
