# Módulo heapq - implementa uma fila de prioridades

import heapq

idades = [15, 10, 20, 18, 25, 8, 19]

# print(f'3 Menores idades: {heapq.nsmallest(3, idades)}') # Imprime as 3 menores idades
# print(f'Menor idade: {heapq.nsmallest(1, idades)}') # Imprime a menor idade
# print()
# print(f'3 Maiores idades: {heapq.nlargest(3, idades)}') # Imprime as 3 maiores idades
# print(f'Maior idade: {heapq.nlargest(1, idades)}') # Imprime a maior idade

heapq.heapify(idades) # transforma lista em heap
print(idades)
print(idades[0]) # menor idade

heapq.heappop(idades) # sempre remove o menor elemento
print(idades)
heapq.heappop(idades)
print(idades)
heapq.heappop(idades)
print(idades)

heapq.heappush(idades, 4) # insere na heap
print(idades)