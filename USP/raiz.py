a = int(input('Digite um valor para \'a\': '))
b = int(input('Digite um valor para \'b\': '))
c = int(input('Digite um valor para \'c\': '))

D = (b**2 - 4*a*c)
x1 = (-b + D**(1/2)) / (2*a)
x2 = (-b - D**(1/2)) / (2*a)


if (D < 0):
   print('esta equação não possui raízes reais')
elif (D == 0):
    print('a raiz desta equação é', x1)
else:
    if (x1 < x2):
        print('as raízes da equação são', x1, 'e', x2)
    else: 
        print('as raízes da equação são', x2, 'e', x1)