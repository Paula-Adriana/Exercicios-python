# Refaça o exercício E01S07_retangulo.py imprimindo os retângulos sem preenchimento, de forma que os caracteres
# que não estiverem na borda do retângulo sejam espaços.

largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
x = 1 
while x <= altura: 
   print('#' * largura, end = '') 
   print() 
   x += 1 
   while x > 1 and x < altura: 
      print('#' + ' ' * (largura - 2) + '#') 
      x += 1 