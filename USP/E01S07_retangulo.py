# Escreva um programa que recebe como entradas dois números inteiros correspondentes à largura e à altura de um 
# retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o retângulo 
# informado com caracteres '#' na saída.
largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))

while altura != 0:
    x = largura
    print(end='\n')
    while largura != 0:
        print('#', end='')
        largura -= 1
    altura -= 1
    largura = x
  
    