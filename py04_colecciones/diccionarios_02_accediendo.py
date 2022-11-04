# Si deseamos acceder a un elemento del diccionario, se puede hacer haciendo
mi_diccionario = {
    "fire": "fuego",
    "water": "agua",
    "earth": "tierra",
    "wind": "viento",
}


# 1. referencia a su clave colocándola dentro de corchetes (ejemplo 1)
elemento1 = miDiccionario["water"]  # haciendo referencia a su clave dentro de corchetes
print(elemento1)  # salida: agua


# 2. utilizando el método get()
elemento2 = miDiccionario.get("earth")  # utilizando el método get()
print(elemento2)  # salida: tierra
