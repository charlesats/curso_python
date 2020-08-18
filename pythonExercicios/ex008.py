# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela
# o nome do escolhido#
import random
nome0 = input('Digite um nome: ')
nome1 = input('Digite um nome: ')
nome2 = input('Digite um nome: ')
nome3 = input('Digite um nome: ')

escolhido = random.choice([nome0, nome1, nome2, nome3])

print('O aluno escolhido para apagar o quadro foi {}'.format(escolhido))
