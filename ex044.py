print('\n{:=^40}'.format(' LOJAS CARMO '))

valor = float(input('\nDigite o valor do produto (R$): '))
avista = valor - (valor * 10 / 100)
avistacartao = valor - (valor * 5 / 100)
duasvezes = valor / 2
tresvezes = valor + (valor * 20 / 100)

formapag = str(input('''\nFORMA DE PAGAMENTO:
[1] Á vista - 10% de desconto
[2] Á vista no crédito - 5% de desconto
[3] 2x no crédito - preço original
[4] 3x ou mais no crédito - 20% de juros no valor total
\nSelecione a opção: ''')).strip()

if formapag == '1':
    print('\nO valor a pagar é de R${:.2f}'.format(avista))
elif formapag == '2':
    print('\nO valor a pagar é de R${:.2f}'.format(avistacartao))
elif formapag == '3':
    print('\nO valor a pagar será em 2x de R${:.2f}, totalizando R${:.2f}'.format(duasvezes, valor))
elif formapag == '4':
    parcelas = int(input('\nQuantas parcelas? '))
    print('\nO valor a pagar será em {}x de R${:.2f}, totalizando R${:.2f}'.format(parcelas, tresvezes / parcelas, tresvezes))
else:
    print('\nOpção inválida!')
