# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

a = 1
b = 1
num = int(input('Informe até qual número gerar a sequência: '))

while (a <= num):
   print(a, b, end=' ')
   a = a + b
   b = a + b
   
    

