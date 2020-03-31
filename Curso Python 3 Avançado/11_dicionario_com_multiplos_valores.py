# Dicionário com múltiplos valores

from collections import defaultdict

dic = defaultdict(list) # list use append

dic['Geisla'].append(19) 
dic['Geisla'].append(17)
dic['Geisla'].append(3)
print(dic['Geisla'])

print()

dic['Vinícius'].append(24)
dic['Vinícius'].append(17)
print(dic['Vinícius'])

dic = defaultdict(set) # set use add

dic['Geisla'].add(17) 
dic['Geisla'].add(17)
dic['Geisla'].add(3)
print(dic['Geisla'])