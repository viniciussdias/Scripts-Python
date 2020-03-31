# Escrevendo arquivos

arq = open('10_escrevendo_arquivos.txt', 'w')
arq.write('''O coronavírus (COVID-19) é uma doença infecciosa causada por um novo vírus 
que nunca havia sido identificado em humanos. O vírus causa uma doença 
respiratória semelhante à gripe e tem sintomas como tosse, febre e, em casos 
mais graves, pneumonia. É possível se proteger ao lavar as mãos com frequência 
e evitar tocar no rosto.''')
print('Escrita concluída!')
arq.close()