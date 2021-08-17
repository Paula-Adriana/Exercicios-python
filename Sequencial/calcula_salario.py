# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#  Calcule e mostre o total do seu salário no referido mês.

hora = int(input('Qual valor da hora trabalhada: '))
num_horas = int(input('Quantas horas no mês você trabalha?: '))
print('O seu salário no mês é de %.2f' %(hora*num_horas))