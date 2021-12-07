# 3. Si se desea cambiar el valor asociado a una clave especifica, se puede hacer
# haciendo referencia a la clave del elemento, a continuación se muestra un
# ejemplo:
miDiccionario = {
    "fire": "fuego",
    "water": "agua",
    "earth": "tierra",
    "wind": "viento",
}

print(miDiccionario)
print(miDiccionario["fire"])

miDiccionario["fire"] = "fogata"
item = miDiccionario["fire"]  # salida: fogata
print(item)
print(miDiccionario)
