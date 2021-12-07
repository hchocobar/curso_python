""" LABORATORIO 3.1.2.6

Tiempo estimado
5 minutos

Nivel de dificultad
Muy fácil

Objetivos
Familiarizar al estudiante con:
- Utilizar el ciclo for.
- Reflejar situaciones de la vida real en código de computadora.

Escenario

¿Sabes lo que es Mississippi? Bueno, es el nombre de uno de los estados y ríos en los Estados Unidos. El río
Mississippi tiene aproximadamente 2,340 millas de largo (3766 Km), lo que lo convierte en el segundo río más largo de
los Estados Unidos (el más largo es el río Missouri). ¡Es tan largo que una sola gota de agua necesita 90 días para
recorrer toda su longitud!

Pero también se usa para un propósito ligeramente diferente: para contar mississippily (mississippimente).

Si no estás familiarizado con la frase, estamos aquí para explicarte lo que significa: se utiliza para contar segundos.

La idea detrás de esto es que agregar la palabra Mississippi a un número al contar los segundos en voz alta hace que
suene más cercano al reloj, y por lo tanto "un Mississippi, dos Mississippi, tres Mississippi" tomará aproximadamente
unos tres segundos reales de tiempo. A menudo lo usan los niños que juegan al escondite para asegurarse de que el
buscador haga un conteo honesto.

Tu tarea es muy simple aquí: escribe un programa que use un ciclo for para "contar de forma mississippi" hasta cinco.
Habiendo contado hasta cinco, el programa debería imprimir en la pantalla el mensaje final "¡Listo o no, ahí voy!"

INFO EXTRA

Ten en cuenta que el código en el editor contiene dos elementos que pueden no ser del claros en este momento: la
declaración import time y el método sleep(). Vamos a hablar de ellos pronto.

Por el momento, nos gustaría que supieras que hemos importado el módulo time y hemos utilizado el método sleep() para
suspender la ejecución de cada función posterior de print() dentro del ciclo for durante un segundo, de modo que el
mensaje enviado a la consola se parezca a un conteo real. No te preocupes, pronto aprenderás más sobre módulos y
métodos.

Salida esperada
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
¡Listo o no, ahí voy!

Código Propuesto:
import time

    # Escribe un ciclo for que cuente hasta cinco.
    # Cuerpo del ciclo: imprime el número de iteración del ciclo y la palabra "Mississippi".
    # Cuerpo del ciclo - uso: time.sleep (1)

# Escribe una función de impresión con el mensaje final.

"""
import time

for i in range(5):
    print(i + 1, "Mississippi")
    time.sleep(1)
print("¡Listo o no, ahí voy!")
