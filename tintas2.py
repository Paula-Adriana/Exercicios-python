# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#  Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima,
#  isto é, considere latas cheias.

metros = float(input('Qual o tamanho da área? '))
litros = (metros/6)
numLatas = (round((litros/18) + 0.5))
numGalao = (round((litros/3.6) + 0.5))
precoLata = numLatas*80
precoGalao = numGalao*25
print (numLatas, 'latas. Preço total: R$ %.2f' %precoLata, 'reais.')
print (numGalao, 'galões. Preço total: R$ %.2f' %precoGalao, 'reais.')

#mix
mixLata = int(litros/18)
mixGalao = int((litros - (mixLata*18))/3.6)
if ((litros - (mixLata * 18.0) % 3.6 != 0)):
    mixGalao += 1
print(mixLata, 'latas e', mixGalao, 'galões serão necessários.'
' Preço total: R$', (mixLata*80) + (mixGalao*25), 'reais.')
