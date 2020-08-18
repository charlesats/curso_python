#Faça um programa que leia o valor de um ângulo qualquer e
#mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('Para o ângulo {},\nO valor do Seno é {:.2f},\nO valor do Cosseno é {:.2f}\nO valor da Tangente é {:.2f}'.format(angulo, sen, cos, tan))
