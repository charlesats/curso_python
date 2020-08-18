# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros#

print('=-=' * 5, 'Lojas do Charlin', '=-=' * 5)
valor = float(input('Valor das compras: '))
print('Forma de Pagamento\n[1] - À vista no dinheiro\n[2] - À vista no cartão\n[3] - 2 x no cartão\n[4] - 3 x no cartão')
opcao = int(input('Digite uma opção: '))

if opcao == 1:
    total = valor - (valor * 0.1)
    print('O valor total a ser pago é: R${:.2f}'.format(total))
elif opcao == 2:
    total = valor - (valor * 0.05)
    print('O valor total a ser pago é: R${:.2f}'.format(total))
elif opcao == 3:
    parcela = valor / 2
    print('O valor de R${:.2f} será pago em 2 x R${:.2f}'.format(valor,parcela))
elif opcao == 4:
    total = valor + (valor * 0.2)
    parcela = total / 3
    print('O valor de R${:.2f}, com 20% de juros, será pago em 3 x R${:.2f}'.format(total, parcela))
else:
    print('Opção incorreta, tente novamente!')
print('=-=' * 16)
