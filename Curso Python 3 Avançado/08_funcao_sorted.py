# Função Sorted - ordenar elementos crescentemente
'''
# ordenar lista
print('== ORDENAR LISTA ==')
lista = [10, 5, 11, 3, 20, 18]
print(f'Lista desordenada: {lista}')
print(f'Lista ordenada: {sorted(lista)}')
print()
# ordenar tupla
print('== ORDENAR TUPLA ==')
tupla = ('Python', 'Java', 'PHP', 'C++', 'HTML')
print(f'Tupla desordenada: {tupla}')
print(f'Tupla ordenada: {sorted(tupla)}')
print()
# ordenar dicionário
print('== ORDENAR DICIONÁRIO ==')
dic = {3:'b', 1:'a', 2:'c'}
print(f'Dicionário desordenado: {dic}')
print(f'Dicionário ordenado: {sorted(dic)}') # retorna lista ordenada pela chave
'''

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return self.nome

def peloNome(pessoa):
    return pessoa.nome

def pelaIdade(pessoa):
    return pessoa.idade

p1 = Pessoa('Geisla', 22)
p2 = Pessoa('Vinícius', 21)
p3 = Pessoa('Carlos', 8)

pessoas = [p1, p2, p3]

print(sorted(pessoas, key=peloNome)) # key define o critério de ordenação
print(sorted(pessoas, key=pelaIdade, reverse=True)) # ordem reversa

