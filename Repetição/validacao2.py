# Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = ''
while (len(nome) <= 3):
    nome = input('Digite seu nome: ')
    if (len(nome) <= 3):
        print('O nome deve conter mais de 3 caracteres')

idade = -1
while (idade < 0 or idade >= 150):
    idade = int(input('Digite sua idade: '))
    if (idade < 0 or idade >= 150):
        print('A idade deve estar entre zero e 150 anos.')

salario = 0
while (salario <= 0):
    salario = float(input('Digite seu salário: '))
    if (salario <= 0):
        print('O salário deve ser maior que zero.')

sexo = ''
while (sexo != 'F' and sexo != 'M'):
    sexo = input('Digite seu sexo: ').upper()
    if (sexo != 'F' and sexo != 'M'):
        print('O sexo deve ser M (masculino) ou F (feminino)')

estado_civil = 'X'
while ('SCVD'.find(estado_civil) < 0):
    estado_civil = input('Digite seu estado civil: ').upper()
    if ('SCVD'.find(estado_civil) < 0):
        print('O estado civil deve ser: S - Solteiro(a) | C - Casado(a) | V - Viúvo(a) | D - Divorciado(a)')

