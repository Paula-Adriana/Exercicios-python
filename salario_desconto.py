# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário 
# no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que
#  nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

hora = int(input('Qual valor da hora trabalhada? '))
num_horas = int(input('Quantas horas no mês você trabalha? '))
sal_bruto = hora*num_horas
inss = sal_bruto*0.08
ir = sal_bruto*0.11
sind = sal_bruto*0.05
sal_liq = sal_bruto - inss - ir - sind
print('Salário bruto: R$ %.2f ' %sal_bruto, 'reais.')
print('INSS (8%): R$ ', inss, 'reais.')
print('IR (11%): R$ ' , ir, 'reais.')
print('Sindicato (5%): R$ ',sind, 'reais.')
print('Salário líquido: R$ %.2f ' %sal_liq, 'reais.')
