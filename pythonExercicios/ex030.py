# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o
# maior valor que estão na tupla.

from random import randint

vetor  = randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0 ,1000), randint(0, 1000)

print(vetor)

print(f'Na tupla {vetor}\nO maior valor é {sorted(vetor)[-1]}\nO menor valor é {sorted(vetor)[0]}')
