# Multisets - generalização de conjutos

from collections import Counter # implementa multisets

c = Counter(a=3, b=4, c=2)
c.elements()
print(list(c.elements())) # coleção não ordenada

print(c.most_common()) # elementos mais comuns
print(c.most_common(2)) # os dois elementos mais comuns