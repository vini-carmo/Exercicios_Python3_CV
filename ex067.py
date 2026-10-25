while True:     # Aqui é um comando de laço infinito, para o while rodar independente de condição alguma (enquanto for verdadeiro, execute tal ação)
    n = int(input('\nQuer ver a tabuada de qual número? '))     # Aqui "n" recebe do usuário o número que ele deseja ver a tabuada do 1 ao 10
    print('-' * 45)
    if n < 0:       # Aqui se em "n" for digitado um número negativo (menor que 0), o programa encerra
        break
    for c in range(1, 11):      # Aqui é para o laço "for" rodar 10 vezes
        print(f'{n} x {c} = {n * c}')       # Mostra e calcula a tabuada digitada em "n" 10 vezes
    print('-' * 45)
print('\nPROGRAMA TABUADA ENCERRADO!')
