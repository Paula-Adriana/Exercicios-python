# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

fahr = int(input('Qual é a temperatura em Fahrenheit: '))
C = 5*((fahr-32)/9)
print(fahr, 'fahrenheit são %.2f' %C, 'celsius.')