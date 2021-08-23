valor = int(input('Qual valor para saque? (Mínimo: R$ 10,00 | Máximo: R$ 600,00. '))
if (valor < 10 or valor >600):
    print('Valor inválido!')
else:
    nota_100 = int(valor/100)
    nota_50 = int((valor - (nota_100*100))/50)
    nota_10 = int((valor - (nota_100*100) - (nota_50*50))/10)
    nota_5 = int((valor - (nota_100*100) - (nota_50*50) - (nota_10*10))/5)
    nota_1 = (valor - (nota_100*100) - (nota_10*10) -(nota_50*50) - (nota_5*5))

    print('Notas de 100: ', nota_100)
    print('Notas de 50: ', nota_50)
    print('Notas de 10: ', nota_10)
    print('Notas de 5: ', nota_5)
    print('Notas de 1: ', nota_1)