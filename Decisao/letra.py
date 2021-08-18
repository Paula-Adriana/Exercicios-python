# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vog_lista = ['A', 'E', 'I', 'O', 'U']
letra = input('Digite uma letra: ')
if (letra.upper() in vog_lista): # Outra forma: 'AEIOU'.find(letra.upper())
    print('Você digitou uma vogal.')
else:
    print('Você digitou uma consoante.')

