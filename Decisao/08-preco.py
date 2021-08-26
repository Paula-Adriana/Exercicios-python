# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo
#  mais barato.

prod1 = float(input('Digite o preço do primeiro produto: '))
prod2 = float(input('Digite o preço do segundo produto: '))
prod3 = float(input('Digite o preço do terceiro produto: '))

if (prod1 < prod2 and prod1 < prod3):
    print('Você deverá comprar o produto 1 (R$', prod1,') por ser o mais barato.')
elif (prod2 < prod3):
    print('Você deverá comprar o produto 2 (R$', prod2,') por ser o mais barato.')
else:
    print('Você deverá comprar o produto 3 (R$', prod3,') por ser o mais barato.')
