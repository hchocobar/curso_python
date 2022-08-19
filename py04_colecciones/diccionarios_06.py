# Si deseas examinar los elementos (claves y valores) del diccionario, puedes emplear el método items()
miDiccionario = {
    "fire": "fuego",
    "water": "agua",
    "earth": "tierra",
    "wind": "viento",
}
for variable_01, variable_02 in miDiccionario.items():
    print("Par clave/valor del diccionario ->", variable_01, ":", variable_02)

# Los elementos de la miDiccionario.items() han sido "desempaquetados" en las variables miClave, miValor
