# Combinando elementos em tuplas 
# Utilizando o zip

'''
A zip()função retorna um objeto zip, que é um iterador de tuplas em que o primeiro item em cada iterador passado é emparelhado e, em seguida, o segundo item em cada iterador passado é emparelhado etc.
'''

r = zip([1, 2, 3], [1, 2, 4])
print(type(r))
print(list(r))
