# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
a = 0
b = 1
i = 0
num = int(input('Quantos números da sequência de Fibonacci deseja gerar? '))
print (a, end=' ')
print(b, end=' ')
while (i <= num - 1):
   c = a+b
   print(c, end=' ')
   i += 1
   a = b
   b = c

  
