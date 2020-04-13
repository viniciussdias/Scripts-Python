# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

d = float(input('Uma distância em metros: '))
print(f'A distância de {d}m corresponde a:')
print(f'{d / 1000}km\n{d / 100}hm\n{d / 10}dam\n{d * 10:.0f}dm\n{d * 100:.0f}cm\n{d * 1000:.0f}mm')