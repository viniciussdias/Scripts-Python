# Ordenando uma lista de dicionários

from operator import itemgetter

linhas = [{'nome':'Geisla', 'idade':22},
          {'nome':'JaumBot', 'idade':18},
          {'nome':'SilvaBot', 'idade':14},
          {'nome':'Vinícius', 'idade':21}]

linhas_pelo_nome = sorted(linhas, key=itemgetter('nome'))
linhas_pela_idade = sorted(linhas, key=itemgetter('idade'))

print(linhas_pelo_nome)
print(linhas_pela_idade)

