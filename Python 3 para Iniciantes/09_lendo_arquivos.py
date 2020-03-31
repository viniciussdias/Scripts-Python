# Lendo arquivos

# arq = open('09_lendo_arquivos.txt', 'r')
# print(arq.read())

with open('09_lendo_arquivos.txt', 'r') as f:
    print(f.read())
f.close()