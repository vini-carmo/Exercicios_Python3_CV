numero = int(input('\nDigite um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'. format(c), end=' ')
print('\n\033[m\nO número {} foi divisível {} vezes.'.format(numero, total))
if total == 2:
    print('\nPor isso, ele É PRIMO!')
else:
    print('\nPor isso, ele NÂO É PRIMO!')
