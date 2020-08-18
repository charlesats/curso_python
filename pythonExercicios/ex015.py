# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o nome completo de uma pessoa: \n'))
print('O primeiro nome da pessoa é: {}'.format(nome.split()[0]))
tam = len(nome.split()) - 1
print('O último nome da pessaoa é: {}'. format(nome.split()[tam]))
