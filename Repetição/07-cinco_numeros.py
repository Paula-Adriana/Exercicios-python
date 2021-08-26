# Faça um programa que leia 5 números e informe o maior número.


lista_numeros = []
for i in range (5):
    num = int((input('Informe um número: ')))
    lista_numeros.append(num)
print('O maior valor digitado foi: ', max(lista_numeros))
