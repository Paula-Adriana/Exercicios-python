# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a
#  função de potência da linguagem.

print("base ^ expoente:")
base=int(input("Base: "))
expoente=int(input("Expoente: "))

potencia=1

for i in range(expoente):
    potencia *= base # potencia *= base é igual a: potencia = potencia * base
    i += 1

print(base,'^',expoente,'=',potencia)