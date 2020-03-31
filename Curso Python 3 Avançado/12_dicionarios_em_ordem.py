# Dicionários em ordem

from collections import OrderedDict

dict = OrderedDict() # dicionários em ordem
dict['Python'] = 10
dict['Java'] = 8
dict['PHP'] = 3
dict['JavaScript'] = 6
print('Mantém a ordem de inserção')
for key in dict:
    print(key, dict[key])

