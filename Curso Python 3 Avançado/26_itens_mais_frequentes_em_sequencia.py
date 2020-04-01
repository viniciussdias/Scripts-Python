# Itens mais ferquentes em uma sequência

from collections import Counter

nomes = ['Geisla', 'BotSilva', 'Geisla', 'Vinícius', 'BotJaum', 'Geisla', 'Vinícius']
nomes_cont = Counter(nomes)

print(nomes_cont.most_common(2)) # dois nomes mais frequentes