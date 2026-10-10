maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso da {}a pessoa (KG): '.format(p)))      # Aqui lê o peso de 5 pessoas
    if p == 1:                      # Aqui verifica se só haverá uma entrada de dados, pois se houver, esse número será o maior e o menor peso ao mesmo tempo
        maior = peso
        menor = peso
    else:                           # Se não, então abre duas condicionais:
        if peso > maior:            # Se o peso for o maior digitado, então a variável "maior" receberá esse valor
            maior = peso
        if peso < menor:            # Se o peso for o menor digitado, então a variável "menor" receberá esse valor
            menor = peso
print('\nO maior peso lido foi {}KG'.format(maior))
print('O menor peso lido foi {}KG'.format(menor))
