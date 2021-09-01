num = int(input('Digite um número inteiro: '))

if (num == 0) or (num == 1):
    print('não primo')
elif ((num == 2) or (num == 3) or (num == 5) or (num == 7)):
     print('primo')
else:
    if (num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0):
        print('não primo')
    else:
        print('primo')