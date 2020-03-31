# Cálculos com dicionários

d = {'tablet':2000, 'notebook':3000, 'iphone':5000}

min_preco = min(zip(d.values(), d.keys()))
print(min_preco)
max_preco = max(zip(d.values(), d.keys()))
print(max_preco)
