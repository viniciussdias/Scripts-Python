# Listas - Estrutura de dados

# Lista é heterogênea, pode ter elementos de diversos tipos.

lista = [] # lista vazia

lista = [1, 2, 3, 4]
print(lista)

lista = [1, 2, 'Bola', 3.14]
print(lista)

# Python indexa a partir do 0.

print(lista[0]) # primeiro elemento
print(lista[-1]) # último elemento

# Inserir na lista
lista.append('Dias')
print(lista)

# Tamanho da lista
print(len(lista))

# Extender lista
lista2 = ['Eu', 'Amo', 'a', 'Geisla']
lista.extend(lista2)
print(lista)

# Inserir elementos pela posição
lista.insert(0, 'Linda')
print(lista)

# Remover elemento da lista
lista.remove(3.14)
print(lista)

# Remover elemento da lista pela posição
lista.pop(1)
lista.pop(2)
lista.pop(3)
print(lista)

# Limpar lista
lista = ['Eu', 'Amo', 'a', 'Geisla']
print(lista)
lista.clear()
print(lista)

# Retornar índice de um elemento
lista = ['Eu', 'Amo', 'Amo', 'a', 'Geisla']
print(lista.index('Geisla'))

# Contar repetição de elementos
print(lista.count('Amo'))

# Ordenar a lista
lista = [10, 2, 5, 4, 1, 8]
print(lista)
lista.sort()
print(lista)
