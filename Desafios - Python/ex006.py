# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada.

num = int(input('Digite um número: '))
print(f'O dobro de {num} vale {num * 2}')
print(f'O triplo de {num} vale {num * 3}')
print(f'A raíz quadrada de {num} é igual a {pow(num, (1/2)):.2f}')