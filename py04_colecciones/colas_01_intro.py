# Implementación de una cola utilizando listas y collections.deque
from collections import deque


# Creamos la cola
queue = deque(["Eric", "John", "Michael"])

# Agregamos elementos al final de la cola
queue.append("Terry")
queue.append("Graham")
print(queue)  # Salida: deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])

# Sacamos elementos del inicio de la cola
queue.popleft()
print(queue)  # Salida: deque(['John', 'Michael', 'Terry', 'Graham'])
queue.popleft()
print(queue)  # Salida: deque(['Michael', 'Terry', 'Graham'])
