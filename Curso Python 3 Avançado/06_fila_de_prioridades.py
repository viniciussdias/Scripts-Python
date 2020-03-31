# Fila de prioridades - Priority Queue:

import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = [] # fila vazia
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item)) # (-priority) da maior prioridade para a menor
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1] # [-1] pega o último elemento da tupla: item

class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome

queue = PriorityQueue()
queue.push(Pessoa('Vinícius'), 21) # insere na fila
queue.push(Pessoa('Geisla'), 22)
queue.push(Pessoa('Yuri'), 14)

print(queue.pop()) # remove da fila maior prioridade

