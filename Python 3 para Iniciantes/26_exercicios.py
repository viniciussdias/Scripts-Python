# Exercícios

# fibonacci
# 1, 1, 2, 3, 5, 8, 13...

print('====== Sequência de Fibonacci ======')
def fib(n):

    if n == 1 or n == 2: # caso base
        return 1
    return fib(n - 1) + fib(n - 2)

termo = int(input('Termo da sequência de Fibonacci? '))
print(f'O {termo}º termo da Sequência de Fibonacci é: {fib(termo)}')

print()

# potência
# 2 ** 3 = 2 * 2 * 2 = 8
# 2 ** 0 = 1

print('====== Potência ======')
def pot(b, e):

    if e == 0:
        return 1
    return b * pot(b, e - 1)

base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))
print(f'{base} elevado a {expoente} é: {pot(base, expoente)}')

print()

# verifica se um número é par
print('====== É par? ======')
def eh_par(num):

    if num % 2 == 0:
        return True
    return False

num = int(input('Digite um número: '))
print(f'{num} é par? {eh_par(num)}')

print()

# verifica se um número é primo
print('====== É primo? ======')
def eh_primo(num):

    if num == 1:
        return False

    div = 0
    for i in range(1, num + 1):
        if num % i == 0:
            div += 1
    return False if div > 2 else True

num = int(input('Digite um número: '))
print(f'{num} é primo? {eh_primo(num)}')