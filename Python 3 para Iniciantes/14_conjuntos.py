# Conjuntos - sets

# Os conjuntos são não ordenados e não permitem elemento repetidos

conjunto = {2, 2, 'Dias', 3, 'Dias'}
print(conjunto)
print(len(conjunto))

# Converter lista para conjunto
lista = [1, 1, 1, 2, 2, 3, 4]
conjunto = set(lista)
print(conjunto)

# Inserir elemento no conjunto
conjunto.add(2) # já tem o elemento 2, logo, não vai inserir
conjunto.add(5)
print(conjunto)

# Remover elemento do conjunto
conjunto.remove(5)
print(conjunto)

# Verificar o tipo de conjunto
print(type(conjunto))