# Faça um programa que leia 5 números e informe a soma e a média dos números.
lista_numeros = []
for i in range (5):
    num = int((input('Informe um número: ')))
    lista_numeros.append(num)
print('A soma dos números digitados foi: ', sum(lista_numeros), 'e a média correspondente é: ',
 (sum(lista_numeros)/len(lista_numeros)))
