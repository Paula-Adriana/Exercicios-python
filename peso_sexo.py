# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('Digite sua altura: '))
pesoH = (72.7*altura) - 58
pesoM = (62.1*altura) - 44.7
print('Se masculino, seu peso ideal é %.2f' %pesoM, 'quilos. Se feminino, %.2f' %pesoM, 'quilos.')