# Strings imutáveis

nome = 'Python'
print(nome)

# class F:

#     def __init__(self, nome):
#         self.nome = nome

# nome = 'Python'
# f = F(nome)
# nome[0] = 'V' -> erro

nome = 'V' + nome[1:] # forma de alterar string
print(nome)
