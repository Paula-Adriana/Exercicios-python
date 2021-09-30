# Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e
#  devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).
def éPrimo(x):
    fator = 2
    if (x == 2):
        return True
    while x % fator != 0 and fator <= x/2:
        fator += 1 
    if (x % fator == 0):
        return False
    else:
        return True

limite = int(input('Limite máximo: '))
n = 2
while n <= limite:
    if éPrimo (n):
        print(n, end=', ')
    n += 1


