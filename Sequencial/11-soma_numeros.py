# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um número inteiro: '))
numR = int(input('Digite um número real: '))
print('O dobro do primeiro com metade do segundo é:', (num1*2)+(num2/2))
print('A soma do triplo do primeiro com o terceiro:', (num1*3)+numR)
print('O terceiro elevado ao cubo é:', (numR**3))


#Outra opcão de exponenciação
# import math
# print('O terceiro elevado ao cubo é:', math.pow(numR, 3))