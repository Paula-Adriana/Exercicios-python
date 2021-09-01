#   Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um
#  dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

num=int(input('Digite um número inteiro: '))

# Para separar último dígito
x = num%10
#números menores que 10 não possuem dígito adjacente igual
if (num < 10):
    print('não')
while num // 10 != 0:

    #descarta o ultimo dígito do número digitado
    num = num//10

    # separar último dígito do 'novo' número
    y = num % 10
    if y==x:
        print('sim')
        break
    # x recebe y para comparação no próximo laço
    x=y
    if num // 10 == 0:
       print('nao')
