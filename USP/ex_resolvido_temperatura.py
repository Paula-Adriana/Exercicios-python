#  Dada uma lista de temperaturas de um mês, informar qual a maior e menor temperatura.

def MinMax (temperaturas):
    print('A menor temperatura do mês foi: ', mínima(temperaturas), 'C')
    print('A maior temperatura do mês foi: ', máxima(temperaturas), 'C')

def mínima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i += 1
    return min

def máxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i += 1
    return max

MinMax([23, 11, 25, 6, 32, 32, 12, 41, 5, 25, 26])
