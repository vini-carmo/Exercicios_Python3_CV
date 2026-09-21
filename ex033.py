n1 = int(input('\nDigite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
menor = n1
# Verificando o menor número
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('\nO menor número é o {}!'.format(menor))
# Verificando o maior número
maior = n2
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n1 and n3 > n2:
    maior = n3
print('\nO maior número é o {}!'.format(maior))
