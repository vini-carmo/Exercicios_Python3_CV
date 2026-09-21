velocidade = float(input('\nDigite sua velocidade em Km/h: '))
if velocidade > 80:
    print('\nVocê foi multado por ultrapassar o limite de 80 Km/h!\n\nTerá que pagar R${:.2f}!'.format((velocidade - 80) * 7))
else:
    print('\nParabéns! Você está dentro do limite permitido.')
