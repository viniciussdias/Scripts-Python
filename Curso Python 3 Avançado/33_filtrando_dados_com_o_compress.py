# Filtrando dados com o compress
# compress seleciona itens que corresponde ao valor True

from itertools import compress

nomes = ['Vinícius', 'Geisla', 'BotJaum', 'BotCar', 'BotSilva']
idades = [21, 22, 17, 16, 30]

maior18 = [i >= 18 for i in idades]
print(maior18)

print(list(compress(nomes, maior18)))