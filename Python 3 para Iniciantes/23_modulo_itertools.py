# Módulo itertools

from itertools import permutations, combinations

lista = [1, 2, 3]

print('Permutações')
for i in permutations(lista):
    print(i)
print('Combinações')
for i in combinations(lista, 2):
    print(i)