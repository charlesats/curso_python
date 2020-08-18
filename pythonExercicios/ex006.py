# Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

import math

cOposto = float(input('Digite o valor do cateto oposto: '))
cAdjacente = float(input('Digite o valor do cateto adjacente: '))
print('O valor da Hipotenusa é {}'.format(math.hypot(cAdjacente, cOposto)))
