# Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
nome = idade = salario = sexo = estado_civil = ''
while (len(nome) < 3) or (idade < 0 and idade >= 150) or (salario < 0) or (sexo != 'f' and sexo != 'm') or (estado_civil != 's' and
estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd'):
    nome = input('Digite seu nome completo: ')
    idade = int(input('Digite sua idade: '))
    salario = float(input('Digite seu salario: '))
    sexo = input('Digite seu sexo (f/m): ')
    estado_civil = input('Digite seu estado civil (s, c, v ou d): ')
    if (len(nome) < 3) or (idade < 0 and idade >= 150) or (salario < 0) or (sexo != 'f' and sexo != 'm') or (estado_civil != 's' and
estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd'):
       print('Verifique suas informações')
    else:
        print('Tudo certo!')