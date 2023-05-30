# Operador in, operador not in
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

print("f" in alfabeto, end=' ')
print("F" in alfabeto, end=' ')
print("1" in alfabeto, end=' ')
print("ghij" in alfabeto, end=' ')
print("Xyz" in alfabeto, end=' ')
# Salida: True False False True False

print()

print("f" not in alfabeto, end=' ')
print("F" not in alfabeto, end=' ')
print("1" not in alfabeto, end=' ')
print("ghi" not in alfabeto, end=' ')
print("Xyz" not in alfabeto, end=' ')
# Salida: False True True False True
