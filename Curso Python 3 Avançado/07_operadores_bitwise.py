# Operadores Bitwise - bit a bit

n1 = 10
n2 = 6
print(bin(n1))
print(bin(n2))

# and
r = n1 & n2 # copia o(s) bit(s) existente(s) em ambos na mesma posição
print(f'AND: {r}')

# or
r = n1 | n2 # copia o(s) bit(s) se existente(s) em qualquer dos operandos
print(f'OR: {r}')

# xor
r = n1 ^ n2 # copia o(s) bit(s) diferente(s) setado(s) em um dos operandos, mas não em ambos
print(f'XOR: {r}')

# complemento de 2
r = (~n1)
print(f'Complemento de 2: {r}')
print(bin(n1))
print(bin(r))

print()

# << move a esquerda
print('Mover para a esquerda')
print(f'{n1}: {bin(n1)}')
print(f'{n1 << 1}: {bin(n1 << 1)}')
print(f'{n1 << 2}: {bin(n1 << 2)}')

print()

# >> move a direita
print('Mover para a direita')
print(f'{n1}: {bin(n1)}')
print(f'{n1 >> 1:2}: {bin(n1 >> 1)}')
print(f'{n1 >> 2:2}: {bin(n1 >> 2)}')



