# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que
#  o usuário informe um valor válido.

nota = int(input('Digite uma nota entre zero e dez: '))
if (nota < 0 or nota > 10):
    print('Valor inválido')
    while (nota < 0 or nota > 10):
        nota = int(input('Digite uma nota entre zero e dez: '))
    if (nota > 0 or nota <= 10):
        print('Você digitou um valor válido de', nota)
