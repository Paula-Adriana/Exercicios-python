# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#  calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arq_mb = int(input('Qual o tamanho em MB do arquivo? '))
veloc = float(input('Qual a velocidade em Mbps de internet? '))
veloc_MBps = veloc/8
#MB = megabyte
#mbps: megabyte por segundo

print('O tempo aproximado de download do arquivo é de', ((arq_mb/veloc_MBps)/60), 'minutos.')