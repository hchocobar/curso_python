# LABORATORIO 3.1.2.3
numeroSecreto = 777

print("""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
# Aquí escribe tu código

number = 0
while numeroSecreto != number:
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    number = int(input("ingresa un número entero para liberarte: "))
print("¡Bien hecho, muggle! Eres libre ahora")
