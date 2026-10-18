n = int(input('\nDigite um número para ser calculado o seu Fatorial: '))    # Aqui "n" recebe o número a ser calculado o fatorial

print('\nCalculando {}! = '.format(n), end='')  # Aqui printa na tela o número a ser calculado o fatorial

f = 1       # Variável "f" recebe o valor 1 para poder multiplicar com o "c" no laço "for"

for c in range(n, 0, -1):       # Aqui o laço "c" roda do número digitado em "n" até 0 de 1 em 1
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')        # Aqui se o contador (c) continuar sendo maior que 1, print ‘ x ’, se não, print ‘ = ’
    f = f * c                                   # Aqui "f" serve para fazer o cálculo do fatorial, multiplicando o valor de "n" vezes o número regredindo de "c" até o 1

print('{}'.format(f))
