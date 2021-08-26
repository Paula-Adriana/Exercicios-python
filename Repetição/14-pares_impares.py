# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
i = 0
par = []
impar = []
while (i < 10):
    num = int(input('Digite um número inteiro: '))
    if (num % 2 == 0):
        par.append(num)
    else:
        impar.append(num)
    i += 1
print('Você digitou', len(par), 'números pares e ', len(impar), 'números ímpares.')

