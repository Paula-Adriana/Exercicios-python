#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
# se digitar outro valor deve aparecer valor inválido.
num = int(input('Digite um número de 1 a 7 para saber o dia da semana: '))
if (num == 1):
    print('Hoje é domingo!')
elif (num == 2):
    print('Hoje é segunda!')
elif (num == 3):
    print('Hoje é terça!')
elif (num == 4):
    print('Hoje é quarta!')
elif (num == 5):
    print('Hoje é quinta!')
elif (num == 6):
    print('Hoje é sexta!')
elif (num == 7):
    print('Hoje é sábado!')
else:
    print('Valor inválido!')
