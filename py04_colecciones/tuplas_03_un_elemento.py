# La tupla de un solo elemento se define de la siguiente manera:
mi_tupla1 = ("uno",)  # Paréntesis y coma
mi_tupla2 = "uno",  # Sin paréntesis, solo la coma
print(mi_tupla1)
print(mi_tupla2)

# Si se elimina la coma, Python creará una variable no una tupla:
mi_tupla1 = 1,
print(type(mi_tupla1))  # Salida: <class 'tuple'>
mi_tupla2 = 1
print(type(mi_tupla2))  # Salida: <class 'int'>
