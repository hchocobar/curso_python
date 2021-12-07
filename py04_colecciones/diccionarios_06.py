# Si deseas examinar los elementos (claves y valores) del diccionario, puedes emplear el método items()
miDiccionario = {
    "fire": "fuego",
    "water": "agua",
    "earth": "tierra",
    "wind": "viento",
}
for miClave, miValor in miDiccionario.items():
    print("Par clave/valor del diccionario ->", miClave, ":", miValor)

# Los elementos de la miDiccionario.items() han sido "desempaquetados" en las variables miClave, miValor
