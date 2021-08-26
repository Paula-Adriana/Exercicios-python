# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de
#  erro e voltando a pedir as informações.


usuario = senha = ''
while (usuario == senha):
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')
    if (usuario == senha):
        print('Acesso negado!! Usuário e senha devem possuir caracteres diferentes.' )
    else:
        print('Acesso permitido!')