casa = float(input('\nQual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100

if prestação > minimo:
    print('\nEMPRÉSTIMO NEGADO!\n\nO valor da prestação seria de R${:.2f} por mês.'.format(prestação), end='')
    print('\n\nIsso excede os 30% do seu salário, que representa R${:.2f}!'.format(minimo))

else:
    print('\nEMPRÉSTIMO APROVADO!\n\nO valor da prestação vai ser de R${:.2f} por mês.'.format(prestação), end='')
    print('\n\nIsso está abaixo dos 30% do salário, que seria R${:.2f}!'.format(minimo))
