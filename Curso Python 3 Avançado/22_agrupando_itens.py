# Agrupando itens com base em uma chave

from operator import itemgetter
from itertools import groupby

exemplos = [('Geisla', 22), ('Vinícius', 21), ('BotJaum', 12), ('Geisla', 17), ('Vinícius', 19), ('BotJaum', 10), ('Geisla', 28)]

exemplos.sort(key=itemgetter(0))
print(exemplos)
print({key: sorted(map(itemgetter(1), value)) for key, value in groupby(exemplos, key=itemgetter(0))})