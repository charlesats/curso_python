# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por
# cada Km acima do limite.

velocidade = int(input('Digite a velocidade do veículo: '))

if velocidade > 80:
    multa = (velocidade-80) * 7
    print('Você foi multado em ${:.2f} reais!'.format(multa))
else:
    print('Velocidade OK!')
