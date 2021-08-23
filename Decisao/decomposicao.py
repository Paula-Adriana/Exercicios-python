#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

num = int(input('Informe um numero inteiro menor que 1000: '))
c = int(num/100)
d = int((num - (c*100))/10)
u = (num - (c*100) - (d*10))

final = ''
if (c > 0):
    final = str(c)
    if (c == 1):
        final = final + ' centena '
    else:
        final = final + ' centenas '

if (d > 0):
    if (c > 0 and u == 0):
        final = final + 'e '
    final = final + str(d)
    if (d == 1):
        final = final + ' dezena '
    else:
        final = final + ' dezenas '


if (u > 0):
    if (c > 0 or d > 0):
        final = final + 'e '
    final = final + str(u)
    if (u == 1):
        final = final + ' unidade '
    else:
        final = final + ' unidades '

print ('O número ', num, ' possui: ', final)