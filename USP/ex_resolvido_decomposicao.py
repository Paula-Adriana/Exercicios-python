# Mostrar a decomposição em fatores primos e a multiplicidade de cada fator de determinado números
# inteiros maior que 1

n = int(input('Digite um número maior que 1: '))
fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade += 1
        n = n/fator
    if (multiplicidade > 0):    
        print('Fator', fator, 'multiplicidade = ', multiplicidade)
    fator += 1 
    multiplicidade = 0