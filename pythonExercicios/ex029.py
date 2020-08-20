# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.#

opcao = 0
while opcao != 5:
    num1 = float(input('Primeiro valor: '))
    num2 = float(input('Segundo valor: '))
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa')
    opcao = int(input('>>>Qual a opção? '))
    if opcao == 1:
        print('A soma é: {}'.format(num1 + num2))
    elif opcao == 2:
        print('A multiplicação é: {}'.format(num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print('O número {} é o maior!'.format(num1))
        elif num2 > num1:
            print('O número {} é o maior!'.format(num2))
        else:
            print('Os números são iguais!')
    elif opcao == 4:
        print('Digite os novos números!')
    elif opcao == 5:
        print('Saindo!')
    else:
        print('Opção inválida! Tente novamente.')
print('Programa encerrado!')
