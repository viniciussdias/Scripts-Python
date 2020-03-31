# Classes - entidades

class Pessoa:

    def __init__(self, nome): # Construtor (recebe parâmetros. O primeiro é o self, que diz respeito a este objeto.)
        self.nome = nome # self diz respeito ao objeto, ou seja, o nome do objeto vai receber o nome passado no parâmetro.

    def obterNome(self):
        return self.nome

    def alterarNome(self, nome):
        self.nome = nome

# Criar instâncias da classe pessoa, ou seja objetos. "Uma pessoa é um objeto"

# pessoa1 = Pessoa('Vinícius')
# print(pessoa1.obterNome())
# pessoa1.alterarNome('Geisla')
# print(pessoa1.obterNome())

p1 = Pessoa('Geisla')
p2 = Pessoa('Vinícius')

pessoas = [p1, p2]

for p in pessoas:
    print(p.obterNome())

