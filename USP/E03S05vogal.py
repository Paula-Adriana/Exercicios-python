# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

def vogal(v):
    if (v.upper() in 'AEIOU'):
         return True
    else:
        return False



print(vogal('a'))