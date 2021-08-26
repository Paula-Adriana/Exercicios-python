# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
data = input('Informe uma data (dd/mm/aaaa): ')

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

valido = False
if (mes in (1, 3, 5, 7, 8, 10, 12)):
    if (dia > 1) and (dia <= 31):
        valido = True
elif (mes in (4, 6, 9, 11)):
    if (dia > 1) and (dia <= 30):
        valido = True
elif (mes == 2):
    if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 400 == 0)):
        if(dia > 1) and (dia <= 29):
            valido = True
    elif(dia > 1) and (dia <= 28):
        valido = True


if (valido):
    print('Data válida')
else:
    print('Data inválida')