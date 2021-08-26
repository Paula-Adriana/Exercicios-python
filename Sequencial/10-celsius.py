# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
cels = int(input('Qual é a temperatura em Celsius: '))
fahr = (cels*(9/5)+32)
print(cels, 'celsius são %.2f' %fahr, 'fahrenheit.')