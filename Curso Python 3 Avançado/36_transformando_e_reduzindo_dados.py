# Transformando e reduzindo dados

lista = [1, 2, 3]

print(f'Soma: {sum(lista)}') # soma dos elemntos da lista
print(f'Min: {min(lista)}') # menor da lista
print(f'Max: {max(lista)}') # maior da lista

sum_pow = sum([i * i for i in lista]) # lista
print(f'Soma dos quadrados: {sum_pow}')

sum_pow = sum(i * i for i in lista) # expressão geradora - mais eficiente em quesito memória
print(f'Soma dos quadrados: {sum_pow}')