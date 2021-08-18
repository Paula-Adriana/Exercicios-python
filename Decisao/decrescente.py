#Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if (num1 > num2 and num1 > num3):
    maior = num1
    print(maior)
elif (num2 > num3):
    maior = num2
    print(maior)
else:
  maior = num3
  print(maior)

if (num1 < num2 and num1 > num3 or num1 > num2 and num1 < num3):
    medio = num1
    print(medio)
elif (num2 < num3 and num2 > num1 or num2 > num3 and num2 < num1):
    medio = num2
    print(medio)
else:
  medio = num3
  print(medio)

if (num1 < num2 and num1 < num3):
    menor = num1
    print(menor)
elif (num2 < num3):
    menor = num2
    print(menor)
else:
  menor = num3
  print(menor)