# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% 
# sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e
# escreva o valor a ser pago pelo cliente.

quiloMaca = float(input('Informe o valor do quilo da maça: '))
quiloMorango = float(input('Informe o valor do quilo do Morango: '))

if (quiloMaca < 5):
    precoMaca = quiloMaca*1.80
else:
    precoMaca = quiloMaca*1.50

if (quiloMorango < 5):
    precoMorango = quiloMorango*2.50
else:
    precoMorango = quiloMorango*2.20

precoTotal = precoMaca+precoMorango
quiloTotal = quiloMaca+quiloMorango

if (quiloTotal > 8) or (precoTotal > 25):
    precoDesconto = (precoTotal - (precoTotal*0.10))
    print('Foram adquiridos', quiloMaca, 'quilo(s) de maça e', quiloMorango, 'quilo(s) de morango. Total de R$: ', precoDesconto)
else:   
    print('Foram adquiridos', quiloMaca, 'quilo(s) de maça e', quiloMorango, 'quilo(s) de morango. Total de R$: ',
     precoTotal)


