# Laboratorio

**Tiempo estimado:** 10 minutos

**Nivel de dificultad:** Fácil

**Objetivos:**

- Familiarizarse con el concepto de variables y trabajar con ellas.
- Realizar operaciones básicas y conversiones.
- Experimentar con el código de Python.

**Escenario:**

Millas y kilómetros son unidades de longitud o distancia.

Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, complemente el programa en el editor para que
convierta de:

- Millas a kilómetros.
- Kilómetros a millas.

No se debe cambiar el código existente. Escribe tu código en los lugares indicados con ###. Prueba tu programa con
los datos que han sido provistos en el código fuente.

Pon mucha atención a lo que está ocurriendo dentro de la función ```print()```. Analiza como es que se proveen múltiples
argumentos para la función, y como es que se muestra el resultado.

Nota que algunos de los argumentos dentro de la función ```print()``` son cadenas (por ejemplo "millas son"), y otros son
variables (por ejemplo millas).

**CONSEJO**

Hay una cosa interesante más que está ocurriendo. ¿Puedes ver otra función dentro de la función ```print()```? Es la
función ```round()```. Su trabajo es redondear la salida del resultado al número de decimales especificados en el
paréntesis, y regresar un valor flotante (dentro de la función ```round()``` se puede encontrar el nombre de la variable,
el nombre, una coma, y el número de decimales que se desean mostrar).

Después de completar el laboratorio, intenta escribir diferentes convertidores, por ejemplo, un convertidor de USD a
EUR, un convertidor de temperatura, etc.


**Resultado Esperado:**

    7.38 millas son 11.88 kilómetros
    12.25 kilómetros son 7.61 millas

**Código propuesto:**

```python
km = 12.25
millas = 7.38

millas_a_km =  # aquí va tu código
km_a_millas =  # aquí va tu código

print(millas, " millas son ", round(millas_a_km, 2), " kilómetros ")
print(km, " kilómetros son ", round(km_a_millas, 2), " millas ")
```