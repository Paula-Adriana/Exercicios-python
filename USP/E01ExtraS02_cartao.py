# Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e
#  o valor da fatura  e imprima (saída de dados) a mensagem com os dados recebidos
cliente = input('Digite o nome do cliente:') 
vencimento = input('Digite o dia de vencimento:')
mes = input('Digite o mês de vencimento:')
fatura = input('Digite o valor da fatura:')
print('Olá,', cliente)
print('A sua fatura com vencimento em', vencimento, 'de', mes, 'no valor de R$', fatura, 'está fechada.')