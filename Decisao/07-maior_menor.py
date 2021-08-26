# Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if (num1 > num2 and num1 > num3):
    print('O maior número digitado foi: ',num1)
elif (num2 > num3):
    print('O maior número digitado foi: ',num2)
else:
    print('O maior número digitado foi: ',num3)

if (num1 < num2 and num1 < num3):
    print('O menor número digitado foi: ',num1)
elif (num2 < num3):
    print('O menor número digitado foi: ',num2)
else:
    print('O menor número digitado foi: ',num3)