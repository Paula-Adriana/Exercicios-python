# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto 
# (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que 
# deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
#  quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% 

hora = float(input('Qual valor da hora trabalhada? '))
num_horas = float(input('Quantas horas no mês você trabalha? '))
sal_bruto = hora * num_horas

if (sal_bruto <= 900):
    impostoIR = 0
elif (sal_bruto <= 1500):
    impostoIR = 5
elif (sal_bruto <= 2500.00):
    impostoIR = 10
else:
    impostoIR = 20

cotaIr = sal_bruto * (impostoIR/100)
fgts = sal_bruto*0.11
sind = sal_bruto*0.03
sal_liq = sal_bruto - cotaIr - sind

print('Salário bruto: R$ %.2f ' %sal_bruto, 'reais.')
print('(-)IR (',impostoIR,'%): R$ ', cotaIr, 'reais.')
print('(-)Sindicato (3%): R$ ',sind, 'reais.')
print('FGTS (11%): R$ ',fgts, 'reais.')
print('Descontos R$ ',sind + cotaIr, 'reais.')
print('Salário líquido: R$ %.2f ' %sal_liq, 'reais.')