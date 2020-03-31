# Dicionários - hash table

dic = {'João':28, 'Vinícius':21, 'Geisla':22}
print(dic)
print(dic['Geisla']) # Idade da Geisla

# Verifica somente as chaves do dicionário
print(dic.keys())

# Deletar elemento do dicionário
del dic['João']
print(dic)

# Verificar se elemento está no dicionário
print('Geisla' in dic)


# Verifica somente os valores do dicionário
print(dic.values())
