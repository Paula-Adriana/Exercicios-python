# Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal 
# lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira 
# lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

def remove_repetidos(lista):
    remove_repetidos = []
    for item in lista:
        if item not in remove_repetidos:
            remove_repetidos.append(item)
    return sorted(remove_repetidos)

lista = [2, 4, 2, 2, 3, 3, 1]
remove_repetidos(lista)
print(remove_repetidos(lista))
