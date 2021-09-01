# Receba um número inteiro positivo na entrada e imprima os  n n primeiros números ímpares naturais.
num = int(input('Digite o valor de n: '))
i = 0

while i <= num:
    if (i %2 != 0):
        print(i)
        num += 1

    i += 1
  
    
    