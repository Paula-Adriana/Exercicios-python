#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.


num = int(input('Digite um número inteiro menor que 1000: '))


centena = int(num/100)
dezena = int((num - (centena*100))/10)
unidade = (num - (centena*100) - (dezena*10))
print('O número', num, 'possui ', centena, 'centena', dezena, 'dezena e', unidade, 'unidade.')
