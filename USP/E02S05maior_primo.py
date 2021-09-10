#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou
# igual ao número passado à função
def maior_primo(k):

    primos = []
    for i in range(k+1):
        count = 0
        for j in range(k+1):
            if i%(j+1) == 0: 
                count += 1
        if count == 2:
            primos.append(i)

    return(max(primos))
print(maior_primo(5))