# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#  File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#  Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#  Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a
#  quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total 
# da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as
#  informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

tipoCarne = input('Informe o tipo de carne que deseja (Filé duplo, Alcatra ou Picanha): ').upper()
quantidade = float(input('Informe quantos quilos deseja: '))
pagamento = input('O pagamento será realizado com o cartão Tabajara? (Sim | Nao) ').upper()
desconto = 5

if (tipoCarne == 'FILÉ DUPLO') or (tipoCarne == 'FILE DUPLO'):
    if (quantidade < 5):
        preco = quantidade*4.90
    else:
        preco = quantidade*5.80

if (tipoCarne == 'ALCATRA'): 
    if (quantidade < 5):
        preco = quantidade*5.90
    else:
        preco = quantidade*6.80

if (tipoCarne == 'PICANHA'):
    if(quantidade < 5):
        preco = quantidade*6.90
    else:
        preco = quantidade*7.80

print('CUPOM FISCAL')
print('Tipo de carne: ', tipoCarne)
print('Quantidade (kg): ', quantidade)
print('Preço total: ', preco)
print('Pagamento com cartão Tabajara: ', pagamento)
if (pagamento == 'SIM'):
    print('Valor de desconto: %.2f' %(preco*(desconto/100)))
    print('Valor pago: %.2f' %(preco - (preco*(desconto/100))))
else:
   print('Valor de desconto: R$ 0,00.')
   print('Valor pago: %.2f' %preco) 




