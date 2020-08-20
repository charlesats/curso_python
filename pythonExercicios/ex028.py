# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

pc = randint(0,10)

print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palpite = int(input('Qual o seu palpite? '))
c = 0
while palpite != pc:
    c += 1
    if palpite > pc:
        print('Menos... Tente mais uma vez.')
        palpite = int(input('Qual o seu palpite? '))
    if palpite < pc:
        print('Mais... Tente mais uma vez.')
        palpite = int(input('Qual o seu palpite? '))
print('Parabéns, acertou com {} tentativas!'.format(c))



