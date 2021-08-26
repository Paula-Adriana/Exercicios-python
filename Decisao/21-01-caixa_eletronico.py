# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada 
# valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.



valor = int(input('Qual valor para saque? (Mínimo: R$ 10,00 | Máximo: R$ 600,00. '))
if (valor < 10 or valor >600):
    print('Valor inválido!')
else:
    nota_100 = int(valor/100)
    nota_50 = int((valor - (nota_100*100))/50)
    nota_10 = int((valor - (nota_100*100) - (nota_50*50))/10)
    nota_5 = int((valor - (nota_100*100) - (nota_50*50) - (nota_10*10))/5)
    nota_1 = (valor - (nota_100*100) - (nota_10*10) -(nota_50*50) - (nota_5*5))

    final = ''
    if (nota_100 > 0):
        final = str(nota_100)
        if (nota_100 == 1):
            final = final + ' nota de 100 '
        else:
            final = final + ' notas de 100 '

    if (nota_50 > 0):
        if (nota_10 == 0 and nota_5 == 0 and nota_1 == 0):
            final = final + 'e '
        final = final + str(nota_50)
        if (nota_50 == 1):
            final = final + ' nota de 50 '
        else:
            final = final + ' notas de 50 '

    if (nota_10 > 0):
        if (nota_5 == 0 and nota_1 == 0):
            final = final + 'e '
        final = final + str(nota_10)
        if (nota_10 == 1):
            final = final + ' nota de 10 '
        else:
            final = final + ' notas de 10 '

    if (nota_5 > 0):
        if (nota_100 != 0 or nota_50 != 0 or nota_10 != 0) and (nota_1 == 0):
            final = final + 'e '
        final = final + str(nota_5)
        if (nota_5 == 1):
            final = final + ' nota de 5 '
        else:
            final = final + ' notas de 5 '

    if (nota_1 > 0):
        final = final + 'e ' + str(nota_1)
        if (nota_1 == 1):
            final = final + ' nota de um '
        else:
            final = final + ' notas de um '

    print ('Você receberá o valor de R$ ', valor, ' em: ', final)