# Laboratorio

**Tiempo Estimado:** 5 minutos

**Nivel de Dificultad:** Muy Fácil

**Objetivos:**

- Familiarizarse con el concepto de comentarios en Python.
- Utilizar y no utilizar los comentarios.
- Reemplazar los comentarios con código.
- Experimentar con el código de Python.

**Escenario:**

El código en el editor contiene comentarios. Intenta mejorarlo: agrega o borra comentarios donde consideres que sea 
apropiado (en ocasiones el remover un comentario lo hace más legible), además, cambia el nombre de las variables
donde consideres que esto mejorará la comprensión del código.

**NOTA:**

Los comentarios son muy importantes. No solo hacen que el programa sea más fácil de entender, también sirven
para deshabilitar aquellas partes de código que no son necesarias (por ejemplo, cuando se necesita probar cierta
parte del código, e ignorar el resto). Los buenos programadores describen cada parte importante del código,
y dan nombres significativos a variables, debido a que en ocasiones es mucho más sencillo dejar el comentario dentro
del código mismo.

Es adecuado utilizar nombres de variables legibles, y en ocasiones es mejor dividir el código en partes con nombres (por
ejemplo en funciones). En algunas situaciones, es una buena idea escribir los pasos de como se realizaron los
cálculos de una forma sencilla y clara.

Una cosa más: puede ocurrir que un comentario contenga una pieza de información incorrecta o errónea, nunca se debe
de hacer eso a propósito.

**Código propuesto:**

```python
# este programa calcula los segundos en cierto número de horas determinadas

a = 2  # número de horas
segundos_hora = 3600  # número de segundos en una hora

print("Horas:", a)  #imprime el número de horas
# print("Segundos en horas:", a * segundos_hora)  # se imprime el número de segundos en determinado número de horas

# aquí también se debe de imprimir un "Adiós", pero el programador no tuvo tiempo de escribirlo
# este es el fin del programa que calcula el número de segundos en 2 horas
```