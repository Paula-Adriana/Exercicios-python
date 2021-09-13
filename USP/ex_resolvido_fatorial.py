# Ler uma sequência de números digitados pelo usuário e, para cada número digitado, informar o seu fatorial
num = int(input('Digite um número inteiro: '))
while num >= 0:
    fatorial = 1
    while num > 1:
        fatorial = fatorial * num
        num = num-1
    print(fatorial)
    num = int(input('Digite um número inteiro: '))