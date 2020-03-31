# Desempacotamento de sequências

# desempacotando lista #
x, y, z = [1, 2, 3] 
# print(x)
# print(y)
# print(z)

# desempacotando tupla #
n1, n2 = ('Geisla', 'Vinícius')
# print(n1)
# print(n2)

# desempacotando string #
a, b, c, d, e = 'hello'
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# desempacotando descartando elementos #
x, y, _ = [1, 2, 3] # descartando o último
# print(x)
# print(y)
_, x, y = [1, 2, 3] # descartando o primeiro
# print(x)
# print(y)

lista = [9, 4, 5, 15, 20]
*n1, n2 = lista # (*) evita a exceção de valores em excesso para desempacotar, sempre será uma lista.
                # Utilidade: Pode desempacotar iteráveis de tamanho desconhecido, evitando exceção.
# print(n1)
# print(n2)

# ---------

notas = [9, 7, 8, 5, 10]
n1, *n2, n3 = notas # descartou a primeira e última nota
# print(n2)

first, *_, last = notas # somente a primeira e última nota
print(first)
print(last)
