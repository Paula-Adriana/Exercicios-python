# Escreva um programa que recebe como entradas dois números inteiros correspondentes à largura e à altura de um 
# retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o retângulo 
# informado com caracteres '#' na saída.
largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
x = 1 
while x <= altura: 
   print('#' * largura, end = '') 
   print() 
   x += 1     