# Dicionários - método get

d = {'Geisla':22, 'Vinícius':21, 'Bot':12}
# print(d['Bot'])
# print(d['blabla']) erro

# if d['blabla']:
#     print('Chave existente')
# else:                                      ERRO
#     print('Chave inexistente')

# print(d.get('Bot'))

if d.get('blabla'):
    print('Chave existente')
else:
    print('Chave inexistente')