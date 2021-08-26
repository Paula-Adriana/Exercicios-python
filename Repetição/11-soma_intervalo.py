# Altere o programa anterior para mostrar no final a soma dos números.
num1 = int(input('Informe um número inteiro: '))
num2 = num1
lista = []
while (num2 <= num1):
    num2 = int(input('Informe outro número inteiro: '))
    if (num2 <= num1):
        print ('O valor final deve ser maior que o valor final!')
        
for i in range (num1,num2):
    lista.append(i)

print(sum(lista))