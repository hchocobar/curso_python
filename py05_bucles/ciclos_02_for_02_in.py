# Ejemplo 1
palabra = "Python es un lenguaje de programación"
for letter in palabra:
    print(letter, end="-")
print()
print(palabra[0])  # Salida: P

# Ejemplo 2
for i in range(1, 100):
    if i % 7 == 0:
        print('numero múltiplos de 7 =', i)

texto = "OpenEDG cPython Institute"
for letter in texto:
    if letter == "P":
        break
    print(letter, end="")  # Salida: OpenEDG c
print()

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")  # Salida: pypypy
print()

foo = ""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    foo = foo + ch
print(foo)  # Salida: john.smith
