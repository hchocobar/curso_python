""" Si se desea cambiar el valor asociado a una clave especifica, se puede hacer
haciendo referencia a la clave del elemento"""
mi_diccionario = {"name": "Joe Doe",
                  "mail": "jdoe@company.com",
                  "city": "Michigan",
                  "country": "United State"}

print(mi_diccionario)
print(mi_diccionario["name"])

mi_diccionario["name"] = "Jane Doe"
item = mi_diccionario["name"]  # Salida: Jane Doe
print(item)
print(mi_diccionario)
