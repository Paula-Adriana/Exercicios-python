# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores 
# de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores,
# sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a = int(input('Digite um valor para \'a\': '))
if (a == 0):
    print('Valor de \'a\' não satisfaz uma equação de 2º grau. Programa encerrado!')
else:
    b = int(input('Digite um valor para \'b\': '))
    c = int(input('Digite um valor para \'c\': '))

D = (b**2 - 4*a*c)
x1 = (-b + D**(1/2)) / (2*a)
x2 = (-b - D**(1/2)) / (2*a)


if (D < 0):
   print('Valor do delta negativo, a equação não possui raízes reais. Programa encerrado!')
elif (D == 0):
    print('Valor do delta é zero, a equação possui apenas uma raiz real : %.2f' %x1)
else:
    print('as raízes da equação são x1 = ', x1, 'e x2 = ', x2)
    