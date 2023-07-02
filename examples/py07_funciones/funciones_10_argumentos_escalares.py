# Argumentos Escalares:
# Una función recibe el valor del argumento, no el argumento en sí
def my_function(n):
    print("Parámetro recibido:", n)
    n += 1
    print("Parámetro incrementado:", n)


var = 1
my_function(var)  # Enviamos el valor de la variable 'var' como argumento
print(var)  # El valor de la variable 'var' (que fue como argumento) sigue sin modificaciones
