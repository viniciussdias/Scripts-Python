# Operações de conjuntos em dicionários

d1 = {'Geisla':17, 'Vinícius':17, 'BotJaum':25}
d2 = {'BotSilva':10, 'Geisla':22, 'Vinícius':21}

print(d1.keys() & d2.keys()) # intercessão
print(d1.keys() - d2.keys()) # diferença