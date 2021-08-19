#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

lado1 = float(input('Informe o primeiro lado: '))
lado2 = float(input('Informe o segundo lado: '))
lado3 = float(input('Informe o terceiro lado: '))

if (((lado1+lado2) > lado3) and ((lado2+lado3) > lado1) and ((lado1+lado3) > lado2)):
    triangulo = True
    print('Os valores informados formam um triângulo.')
else:
    triangulo = False
    print('Os valores informados não formam um triângulo.')

if (triangulo):
    if ((lado1 == lado2) and (lado2== lado3)):
        print('do tipo: equilátero')
    elif ((lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3)):
        print('do tipo: isósceles')
    else:
        print('do tipo: escaleno')