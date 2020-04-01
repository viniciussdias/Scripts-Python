# Utilizando a função itemgetter com min e max

from operator import itemgetter

linhas = [{'idade':22}, {'idade':18}, {'idade':14}, {'idade':21}]

print(min(linhas, key=itemgetter('idade'))) # min
print(max(linhas, key=itemgetter('idade'))) # max