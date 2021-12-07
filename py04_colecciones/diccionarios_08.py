# Se puede emplear la palabra reservada "del" para eliminar un elemento, o un diccionario entero.
# Para eliminar todos los elementos de un diccionario se debe emplear el método clear():
miDiccionario = {
    "fire": "fuego",
    "water": "agua",
    "earth": "tierra",
    "wind": "viento",
}
print(len(miDiccionario))  # salida: 3
print(miDiccionario)

del miDiccionario["fire"]  # elimina un elemento
print(len(miDiccionario))  # salida: 2
print(miDiccionario)

miDiccionario.clear()  # elimina todos los elementos
print(len(miDiccionario))  # salida: 0
print(miDiccionario)

del miDiccionario  # elimina el diccionario
print(miDiccionario)
