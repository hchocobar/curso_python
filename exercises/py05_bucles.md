# Ejercicios

## Ejercicio 1

Crea un bucle `for` que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:

```python
for i in range(1, 11):
    # Tu código aquí
```
 
Solución:
```python
for i in range(0, 11):
    if i % 2 != 0:
        print(i)
```

## Ejercicio 2

Crea un bucle `while` que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:

```python
x = 1
while x < 11:
    # Tu código aquí
```

Solución:

```python
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1
```

## Ejercicio 3

Crea un programa con un bucle `for` y una declaración `break`. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte anterior a @ en una línea. Usa el esqueleto de abajo:

```python
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        # Tu código aquí
```

Solución:
```python
for ch in "john.smith@python.org":
    if ch == "@":
        break
    print(ch, end="")
```

## Ejercicio 4

Crea un programa con un bucle `for` y una declaración `continue`. El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla. Usa el esqueleto de abajo:

```python
for digit in "0165031806510":
    if digit == "0":
        # Tu código aquí
```

Solución:

```python
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
```

## Ejercicio 5

¿Cuál es la salida del siguiente código?

```python
n = 3
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)
```

Solución:

    4
    3
    2
    0 

## Ejercicio 6

¿Cuál es la salida del siguiente código?

```python
n = range(4)
for number in n:
    print(number - 1)
else:
    print(number)
```
Solución:

    -1
    0
    1
    2
    3 

## Ejercicio 7

¿Cuál es la salida del siguiente código?

```python
for i in range(0, 6, 3):
    print(i)
```

Solución:

    0
    3