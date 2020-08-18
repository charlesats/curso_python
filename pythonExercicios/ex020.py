# Escreva um programa em Python que leia um número inteiro
# qualquer e peça para o usuário escolher qual será a base
# de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro para conversão: "))
base = int(input("Para qual base deseja converter:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n"))

if base == 1:
    print('O num {} convertido para binário é {}'.format(num,bin(num)[2:]))
elif base == 2:
    print('O num {} convertido para octal é {}'.format(num,oct(num)[2:]))
elif base == 3:
    print('O num {} convertido para hexadecimal é {}'. format(num,hex(num)[2:]))
else:
    print('Entrada incorreta!!!')
