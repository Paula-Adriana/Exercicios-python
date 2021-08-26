# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou 
# “REPROVADO” # se o conceito for D ou E.

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota2+nota1)/2

if (media > 9.0):
    conceito = 'A'
elif (media > 7.5):
    conceito = 'B'
elif (media > 6):
    conceito = 'C'
elif (media > 4):
    conceito = 'D'
else:
    conceito = 'E'

if (conceito == 'A' or conceito == 'B' or conceito == 'C'):
    aprovacao = '- Aprovado'
else:
    aprovacao = '- Reprovado'

print('Suas notas: ', nota1, 'e', nota2, '. Média: ', media, 'Conceito:', conceito, aprovacao)


