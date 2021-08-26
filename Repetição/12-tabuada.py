# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual
#  numero ele deseja ver a tabuada. 

num = -1
while(num < 0) or (num > 10):
    num = int(input('Informe um número de 1 a 10 que deseja ver a tabuada: '))
for i in range (1,11):
    print(num, 'x', i, '=', i*num)
       