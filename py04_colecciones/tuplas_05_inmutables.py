# Las tuplas son inmutables,
# Esto significa que no se puede agregar, modificar, cambiar o quitar elementos.
# El siguiente fragmento de código provocará una excepción:
mi_tupla = (1, 2.0, "cadena", [3, 4], (5, ), True)
mi_tupla[2] = "guitarra"  # se levanta una excepción

# TypeError: 'tuple' object does not support item assignment
