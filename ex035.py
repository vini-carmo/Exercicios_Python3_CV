print('=-' * 20)
print('        Analisador de Triângulos     ')
print('=-' * 20)
r1 = float(input('\nPrimeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nÉ possível fazer um triângulo!')
else:
    print('\nNÃO é possível fazer um triângulo!')
