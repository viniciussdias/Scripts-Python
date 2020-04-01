# Operações matemáticas com Counter

from collections import Counter

a = Counter([1, 1, 2, 2, 2, 3, 4])
b = Counter([2, 3, 4, 5, 6, 6, 7])
c = a + b
print(c)