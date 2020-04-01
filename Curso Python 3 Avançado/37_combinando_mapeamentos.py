# Combinando mapeamentos

from collections import ChainMap

a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

# combinando
c = ChainMap(a, b)
print(c)

print(c['x']) # primeiro mapa
print(c['y']) # segundo mapa
print(c['z']) # primeiro mapa - quanda há chaves duplicadas pega o valor do primeiro mapeamento

# deletando chave
# del c['x']

# combinando com update
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])
