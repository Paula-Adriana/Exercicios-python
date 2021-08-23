# Faça um Programa que leia um número e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve
#  ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

num = float(input('Digite um número: '))
print ('1 - Par ou Impar')
print ('2 - Positivo ou Negativo')
print ('3 - Inteiro ou Decimal')
operacao = input('Qual operação deseja realizar? ')

if (operacao == '1'):
    if (num % 2 == 0):
        print ('O número', num, 'é par!')
    else:
        print ('O número', num, 'é ímpar!')
if (operacao == '2'):
    if (num > 0):
        print ('O número', num, 'é positivo!')
    else:
        print ('O número', num, 'é negativo!')
if (operacao == '3'):
    if (num < round(num)):
        print ('O número', num, 'é decimal!')
    else:
        print ('O número', num, 'é inteiro!')

