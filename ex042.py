r1 = float(input('\nPrimeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nÉ possível fazer um triângulo ', end='')

    if r1 == r2 == r3:
        print('EQUILÁTERO: todos os lados iguais!')

    elif r1 != r2 != r3 != r1:
        print('ESCALENO: todos os lados diferentes!')

    else:
        print('ISÒSCELES: dois lados iguais, um diferente!')

else:
    print('\nNÂO podem formar um triângulo!')
