# Ejemplo 1
palabra = "Python"
for letter in palabra:
    print(letter, end="*")
print()

# Ejemplo 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

texto = "OpenEDG Python Institute"
for letter in texto:
    if letter == "P":
        break
    print(letter, end="")
print()

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")
print()

foo = ""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    foo = foo + ch
print(foo)
