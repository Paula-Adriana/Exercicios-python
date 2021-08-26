# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população
#  de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários
#  que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

pais_A = 8000
pais_B = 20000
anos = 1
while (pais_A <= pais_B):
    pais_A = (pais_A +(pais_A*0.03))
    pais_B = (pais_B +(pais_B*0.015))
    anos += 1
    print(anos, pais_A, pais_B)
       
    
print('Serão necessários',anos+1, 'para que a população do pais A ultrapasse ou iguale a população do país B.')
