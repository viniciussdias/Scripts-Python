# Faça um programa que leia o nome, o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado, e mostre também uma mensagem com a data formatada.

nome = str(input('Qual é o seu nome? '))
dia = int(input('Dia de nascimento: '))
mes = str(input('Mes de nascimento: '))
ano = int(input('Ano de nascimento: '))

print(f'É um prazer te conhecer, {nome}!')
print(f'Você nasceu no dia {dia} de {mes} de {ano}. Correto?')


