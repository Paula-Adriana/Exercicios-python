# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
num1 = int(input('Informe um número inteiro: '))
num2 = num1
while (num2 <= num1):
    num2 = int(input('Informe outro número inteiro: '))
    if (num2 <= num1):
        print ('O valor final deve ser maior que o valor final!')
        
for i in range (num1,num2):
     print(i, ' ', end='')

