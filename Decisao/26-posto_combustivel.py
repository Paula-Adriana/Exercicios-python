# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool: até 20 litros, desconto de 3% por litro. acima de 20 litros, desconto de 5% por litro
# Gasolina:até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
# litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.


litros = float(input('Informe o número de litros vendidos: '))
tipo_combust = input('Informe o tipo de combustível sendo: A-álcool e G-gasolina: ')


if (tipo_combust.upper() == 'A'):
    if (litros <= 20):
        preco = (litros*1.90)
        precoDesconto = (preco - (preco*0.03))
    else:
        preco = (litros*1.90)
        precoDesconto = (preco - (preco*0.05))
if (tipo_combust.upper() == 'G'):
    if (litros <= 20):
        preco = (litros*2.50)
        precoDesconto = (preco - (preco*0.04))
    else:
        preco = (litros*2.50)
        precoDesconto = (preco - (preco*0.06))

print('O valor a ser pago é: R$ %.2f' %precoDesconto)
