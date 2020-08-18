# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
aAtual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))

if  (aAtual - ano) < 18:
    print('Faltam {} para o seu alistamento!'.format(18 - (aAtual - ano)))
elif (aAtual - ano) == 0:
    print('Você deve se alistar este ano')
elif (aAtual - ano) > 18:
    print('Já passou o tempo do alistamento em {} anos'.format(aAtual - ano - 18))
else:
    print('Data inválida!')

