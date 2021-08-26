# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.
pop_A = 0
crescimento_A = 0
while (pop_A <= 0):
    pop_A = float(input('Informe a população residente no país A: '))
    if (pop_A < 0):
        print('O valor da população \'A\' deve ser positivo')

while (crescimento_A <= 0):
    crescimento_A = float(input('Informe a taxa de crescimento do país A: '))
    if (crescimento_A <= 0):
        print('informe um valor positivo para a taxa de crescimento.')

pop_B = pop_A
while (pop_B <= pop_A):
    pop_B = float(input('Informe a população residente no país B: '))
    if (pop_B <= pop_A):
        print('O valor da população \'B\' deve ser maior que a populaçao \'A\'')

crescimento_B = crescimento_A
while (crescimento_B >= crescimento_A):
    crescimento_B = float(input('Informe a taxa de crescimento do país B: '))
    if (crescimento_B >= crescimento_A):
        print('A taxa de crescimento do país \'B\' deve ser menor que a do pais \'A\'.')

anos = 1
while (pop_A <= pop_B):
    pop_A = pop_A * crescimento_A
    pop_B = pop_B * crescimento_B
    anos += 1
    print(anos, pop_A, pop_B)
       
    
print('Serão necessários',anos+1, 'anos para que a população do pais A ultrapasse ou iguale a população do país B.')