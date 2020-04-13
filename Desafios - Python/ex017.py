# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(co, ca):.2f}') # com módulo
# print(f'A hipotenusa vai medir {(co ** 2 + ca ** 2) ** (1 / 2):.2f}') # sem módulo
