peso = float(input('\nQuanto você pesa? (KG) '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura * altura)
print('\nSeu IMC é de: {:.1f}'.format(imc))

if imc < 18.5:
    print('\nCondição: Magreza')

elif imc < 25:
    print('\nCondição: Peso ideal')

elif imc < 30:
    print('\nCondição: Sobrepeso')

elif imc < 35:
    print('\nCondição: Obesidade grau I')

elif imc < 40:
    print('\nCondição: Obesidade grau II')

else:
    print('\nCondição: Obesidade Mórbida')
