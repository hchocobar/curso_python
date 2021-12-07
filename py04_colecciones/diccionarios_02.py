# Si se deseamos acceder a un elemento del diccionario, se puede hacer haciendo
# referencia a su clave colocándola dentro de corchetes (ejemplo 1) o utilizando
# el método get() (ejemplo 2):
miDiccionario = {
    "fire": "fuego",
    "water": "agua",
    "earth": "tierra",
    "wind": "viento",
}
elemento1 = miDiccionario["water"]  # haciendo referencia a su clave dentro de corchetes
print(elemento1)  # salida: agua
elemento2 = miDiccionario.get("earth")  # utilizando el método get()
print(elemento2)  # salida: tierra
