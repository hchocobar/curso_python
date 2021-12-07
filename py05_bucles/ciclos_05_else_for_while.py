print('Ejecución de else en un ciclo for')
for i in range(5):
    print(i)
else:
    print("else:", i)

print('\nEjecución de else en un ciclo while')
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
