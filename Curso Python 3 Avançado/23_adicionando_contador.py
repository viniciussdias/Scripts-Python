# Adicionando um contador a um iterável

tupla = (1, 2, 3, 4, 5)
for cont, elem in enumerate(tupla): # cada iteração possui uma tupla composta pelo (contador, elemento)
    print(f'Contador: {cont} Elemento: {elem}')