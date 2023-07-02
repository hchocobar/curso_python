# Cadenas

## Recordemos
    • ASCII (128)
    • ASCII extendido (256)
    • UNICODE
    • UCS-4
    • UTF-8
        ◦ Todos los caracteres latinos (y todos los caracteres ASCII estándar) ocupan ocho bits.
        ◦ Los caracteres no latinos ocupan 16 bits.
        ◦ Los ideógrafos CJK (China-Japón-Corea) ocupan 24 bits.

## Definición

Las cadenas son secuencias inmutables.

## Puntos Claves

1. Podemos utilizar la función `len()` para conocer su largo.

2. **Concatenación**. El sigo `+` (más), al ser aplicado a dos cadenas, se convierte en un operador de concatenación y también podemos utilizar el atajo `+=`.

```python
print('palabra' + 's')
print('super' + 'curso')
```

3. **Replicación**. El signo `*` (asterisco), cuando es aplicado a una cadena y a un número (o a un número y cadena) se convierte en un operador de replicación y también podemos utilizar el atajo `*=`.
```python
5. print(5 * 'a')
print('b' * 4)
```

4. **Funciones** `ord()` y `char()`.
- `ord()` nos devuelve el valor del punto de código ASCII/UNICODE de un caracter.
- `chr()` devuelve el caracter correspondiente al valor del punto de código ASCII/UNICODE.

5. **Indexación**. Las cadenas son secuencias (no listas) y podemos recorrerlas utilizando su índice con el comando `for`.

6. **Rodajas**. Todo lo que sabes sobre rodajas o rebanadas es utilizable con las cadenas.

7. **Operadores** `in` y `not in`. Funcionan en las cadenas.

8. **Inmutabilidad**. No están permitidos los métodos `append` ni `insert`. Tampoco borrar un elemento con el comando `del`.

9. **Funciones** `min()` y `max()`. Nos devuelven el caracter de valor ASCII-UNICODE mínimo/máximo.
Nota: En estas dos funciones la cadena no puede estar vacía. Si lo está devolverá error.

10. **Métodos**. La lista completa de métodos se presenta aquí: [Dcoumenación oficial de Python sobre cadenas](https://docs.python.org/3.4/library/stdtypes.html#string-methods).

11. **Conversión de tipos de datos**. La función `str()` puede convertir un número a una cadena.