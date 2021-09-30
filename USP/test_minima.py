def mínima(temps):
    min = 0
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i += 1
    return min
    
def testa_mínima():
    print('Inicializando os testes')
    temp = [-15, -10, 0, 21, 11]
    if mínima(temp) != -15:
        print('Valor errado para array ', temp)
    temp = [0, 2, 5, 8]
    if mínima(temp) != 0:
        print('Valor errado para array ', temp)
    temp = [16, 32, 34, 12, 23, 34, 44, 22, 10, 33, 45]
    if mínima(temp) != 10:
        print('Valor errado para array ', temp)

    print('Finalizando os testes')