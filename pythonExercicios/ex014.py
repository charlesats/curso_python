#  Faça um programa que leia uma frase pelo teclado e
#  mostre quantas vezes aparece a letra “A”, em que
#  posição ela aparece a primeira vez e em que posição
#  ela aparece a última vez.

frase = input('Digite uma frase: \n')
qtd = int(frase.upper().count('A'))
print("A frase contém {} letras A".format(qtd))
ult = frase.upper().rfind('A')
print("Ela aparece pela última vez na posição {}".format(ult))
