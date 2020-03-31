# Permutações

from itertools import permutations

for i in permutations([1, 2, 3]):
    print(''.join(str(x) for x in i))