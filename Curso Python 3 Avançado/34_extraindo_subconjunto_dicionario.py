# Extraindo um subconjunto de um dicionário

precos = {'notebook':2500, 
          'tablet':900, 
          'iphone':5000, 
          'mouse':70,
          'teclado':80
          }

precos2 = {key:value for key, value in precos.items() if value > 100} # compreensão de dicionário
print(precos2)