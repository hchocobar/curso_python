# Implementación de una cola utilizando listas y collections.deque
from collections import deque


# Creamos la cola
queue = deque(["Eric", "John", "Michael"])


# Agregamos elementos al final de la cola
queue.append("Terry")
queue.append("Graham")
print(queue)  # salida: deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])


# Sacamos elementos del inicio de la cola
queue.popleft()
print(queue)  # salida: deque(['John', 'Michael', 'Terry', 'Graham'])
queue.popleft()
print(queue)  # salida: deque(['Michael', 'Terry', 'Graham'])
