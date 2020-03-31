# Deque - collections

'''
Deque é uma Fila Duplamente Terminada, onde os elementos 
podem ser adicionadas ou removidos no início ou no fim.
'''

from collections import deque

'''
fila = deque(maxlen=4) # cria fila
fila.append(1) # insere na fila
fila.append(2)
fila.append(3)
fila.append(4)
fila.append(5) # remove o primeiro elemento e insere na fila, pois o tamanho max é 4.
print(fila)
'''

fila = deque()
fila.append(1)
fila.append(2)
fila.append(3)
fila.appendleft(4) # insere do lado esquerdo da fila
print(fila)
fila.pop() # remove elemento sempre do final
print(fila)
fila.popleft() # remove elemento sempre do início
print(fila)