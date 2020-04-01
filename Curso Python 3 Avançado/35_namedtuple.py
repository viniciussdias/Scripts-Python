# Utilizando namedtuple
# Função de fábrica para criar subclasses de tupla com campos nomeados
# Pode substituir um dicionário caso o mesmo for grande
# Namedtuple é imutável

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['user', 'password'])
login = Subscriber('root', '1234')
# print(login)
# print(login.user)
# print(login.password)

# print(len(login)) # tamanho
user, password = login # desempacotar
print(user)
print(password)

# alterar atributo 
login = login._replace(user='admin')
print(login.user)

