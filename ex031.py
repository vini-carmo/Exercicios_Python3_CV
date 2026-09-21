distancia = float(input('\nQual é a distância da sua viagem em Km? '))
print('\nVocê está prestes a começar uma viagem de {}Km!'.format(distancia))
if distancia <= 200:
    print('\nO preço da sua passagem será de R${:.2f}!'.format(distancia * 0.50))
else:
    print('\nO preço da sua passagem será de R${:.2f}!'.format(distancia * 0.45))
