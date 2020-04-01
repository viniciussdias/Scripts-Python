# Criando agrupamentos de dados

from operator import itemgetter
from itertools import groupby

linhas = [{'nome':'Geisla', 'data':'17/09/2019'},
          {'nome':'JaumBot', 'data':'03/04/2015'},
          {'nome':'SilvaBot', 'data':'03/04/2015'},
          {'nome':'Vinícius', 'data':'17/09/2019'},
          {'nome':'HappyDay', 'data':'17/09/2019'}]

# ordena pela data
linhas.sort(key=itemgetter('data'))

# faz a iteração
for data, itens in groupby(linhas, key=itemgetter('data')):
    print(data)
    for i in itens:
        print(' ', i)