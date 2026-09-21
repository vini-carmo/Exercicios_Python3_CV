salario = float(input('\nQual é o salário do funcionáro? R$'))
if salario > 1250:
    novo = salario + (salario * 10 / 100)
else:
    novo = salario + (salario * 15 / 100)
print('\nQuem ganhava R${:.2f}, agora passa a ganhar R${:.2f}!'.format(salario, novo))
