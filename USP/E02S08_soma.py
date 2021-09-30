# Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um
#  número inteiro correspondente à soma dos elementos da lista recebida.

def soma_elementos(lista):
    soma_elementos = 0
    for item in lista:
        soma_elementos += item
    return soma_elementos


lista = [2, 4, 2, 2, 3, 3, 1]
soma_elementos(lista)
print(soma_elementos(lista))

