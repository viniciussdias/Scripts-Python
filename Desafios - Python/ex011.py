# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litros de tinta, pinta uma área de 2m².

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print(f'Sua parede tem a dimensão de {largura} x {altura} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {area / 2}l de tinta.')