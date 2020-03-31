# Tuplas

# Uma tupla é imutável, ou seja não permite nenhuma alteração após ser criada

# Comparação de lista x tupla

#Lista - mutável/tamanho dinâmico
lista = [1, 2, 3]
print(lista)
lista[0] = 4 # Alterando o valor
print(lista)

#Tupla - imutável/tamanho fixo
tupla = (1, 2, 3)
print(tupla)
tupla[0] = 4 # Alterando o valor -- ERRO --
print(tupla)