# Filtrando elementos de uma sequência

from math import sqrt

lista = [-2, 4, 8, 10, -30]
print([i for i in lista if i > 0]) # imprime só os maiores que 0
print([i for i in lista if i < 0]) # imprime só os menores que 0

# generators
p = (i for i in lista if i > 0)
for i in p:
    print(i)

print([sqrt(i) for i in lista if i >= 3])