# Operações em conjuntos (sets)

c = {1, 2, 3, 4, 5}
print(c)
d = {3, 3, 4, 4, 6, 7}
print(d)
print(type(d))

print(f'União: {c | d}') # união dos conjuntos
print(f'Intercessão: {c & d}') # intercessão dos conjuntos
print(f'Elementos que estão em c e não estão em d: {c - d}')
print(f'Elementos que não estão em ambos: {c ^ d}')