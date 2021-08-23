# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?" #"Esteve no local do crime?" #"Mora perto da vítima?" #"Devia para a vítima?" #"Já trabalhou com a vítima?
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#  Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como 
# "Assassino". Caso contrário, ele será classificado como "Inocente".


perg_1 = input('Telefonou para a vítima? ')
perg_2 = input('Esteve no local do crime? ')
perg_3 = input('Mora perto da vítima? ')
perg_4 = input('Devia para a vítima? ')
perg_5 = input('Já trabalhou com a vítima? ')

perguntas = [perg_1, perg_2, perg_3, perg_4, perg_5]
contagem = perguntas.count('sim')

if (contagem == 0):
    print('Inocente')
elif (contagem <= 2):
    print('Suspeita')
elif (contagem < 4):
    print('Cúmplice')
else: 
    print('Assassino')


