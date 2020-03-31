# Manipulando strings

# String é imutável, porém há um macete

nome = 'Vinícios'
print(nome)
print(nome[0])
print(nome[-1])

# Alterando elemento da string
l_nome = list(nome)
print(l_nome)
l_nome[6] = 'u'
print(l_nome)
print(type(l_nome))
nome = ''.join(l_nome) # junta elementos da lista
print(nome)
print(type(nome))

# verificar tamanho do nome
print(len(nome))

