# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor
#  seja maior que 500.
'''
a = 0
b = 1
i = 0
print (a, end=' ')
print(b, end=' ')
while (i <= 500):
   c = a+b
   print(c, end=' ')
   i += 1
   a = b
   b = c'''
