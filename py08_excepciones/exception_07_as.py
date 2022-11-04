"""Las excepciones son clases y por ellos cuando se genera una excepción se está creando una instancia de esa clase.
Por ello, podemos capturar la excepción en un identificador con el fin de analizar su naturaleza y sacar conclusiones
adecuadas.
Nota: el alcance del identificador solo es dentro del except, y no va más allá. """
try:
    i = int("Hola!")
except Exception as e:
    print(e)
    print(e.__str__())
