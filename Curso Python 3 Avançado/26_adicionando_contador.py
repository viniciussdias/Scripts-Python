# Adicionando um contador a um iterável

tupla = (1, 2, 3, 4, 5)
for count, elem in enumerate(tupla): # cada iteração possui uma tupla composta pelo (contador, elemento)
    print(f'Contador: {count} Elemento: {elem}')