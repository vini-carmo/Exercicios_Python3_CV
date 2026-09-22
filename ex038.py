num1 = int(input('\nPrimeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print('\nO número {} é o maior'.format(num1))
elif num2 > num1:
    print('\nO número {} é o maior'.format(num2))
else:
    print('\nAmbos números são iguais!')
