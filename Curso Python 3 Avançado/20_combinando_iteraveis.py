# Combinando iteráveis

from itertools import chain

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = ['Python', 'Java']
comb = chain(lista1, lista2, lista3) # comb é um objeto, transforma para lista
print(list(comb))
