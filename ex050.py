print('\n')
soma = 0
cont = 0
for c in range(6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('\nA soma dos {} números PARES digitados é {}'.format(cont, soma))
