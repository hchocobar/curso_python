# La palabra reservada 'global' extiende el alcance de una variable incluyendo el cuerpo de las funciones para poder
# no solo leer los valores de las variables sino también modificarlos.
def my_function():
    global var
    print("Valor de la variable var dentro la función antes de la asignación:", var)
    var = 7 * 5
    print("Valor de la variable var dentro la función DESPUÉS de la asignación:", var)
    var = 8


var = 3
my_function()
print("Valor de la variable var fuera de la función:", var)  # ¿Qué valor muestra: 3 o 7 ?
