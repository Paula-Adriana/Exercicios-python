from math import sqrt
x1 = float(input('Digite um valor para x1: '))
x2 = float(input('Digite um valor para x2: '))
y1 = float(input('Digite um valor para y1: '))
y2 = float(input('Digite um valor para y2: '))

d = sqrt(((x1-x2)**2) + ((y1-y2)**2))
if (d < 10):
    print('perto')
else:
    print('longe')