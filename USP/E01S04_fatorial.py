# Escreva um programa que receba um número natural  n n na entrada e imprima  n! n! (fatorial) na saída.
num = int(input('Digite o valor de n: '))
fatorial = 1

while num != 0:
    fatorial = fatorial * num
    num = num-1
print(fatorial)
    
