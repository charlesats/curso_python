# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou
# então o empréstimo será negado.

vImovel = float(input('Digite o valor do imóvel: '))
anos = int(input('Em quantos anos pretende pagar: '))
salario = float(input('Qual o seu salário: '))
sMensal = salario * .3
n = (anos * 12)
prestacoes = vImovel / n

if prestacoes <= sMensal:
    print('Parabéns!\nO emprestimo foi aprovado!\nSerão {} parcelas de R${:.2f}.'.format(n,prestacoes))
else:
    print('O valor do emprestimo não foi aprovado!!')
