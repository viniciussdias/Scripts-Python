# Retornando funções

def pai(num):

    def filho1():
        print('Oi, eu sou o filho 1')

    def filho2():
        print('Oi, eu sou o filho 2')

    try: # tratamento de exceções
        assert num == 20 # verificação de veracidade em tempo de execução
        return filho1
    except AssertionError: # tratamento de exceções
        return filho2

f1 = pai(10)
f2 = pai(20)

f1()
f2()