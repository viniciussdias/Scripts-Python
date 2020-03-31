# Geradores - Generators

''' 
Geradores são iteráveis, ou seja pode percorrer os elementos,
porém os valores são lidos apenas quando necessário, possuindo 
uma avaliação preguiçosa.
'''
# exemplo de iterável
# lista = [1, 2, 3, 4]
# for i in lista:
#     print(i)

# exemplo de generator
gerador = (letra for letra in 'python')
gerador.__next__() # no terminal
# next(gerador) - alternativo a linha anterior

# OBS: o next retorna cada valor do gerador até o final