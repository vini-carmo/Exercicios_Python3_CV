from time import sleep          # Função "sleep" da biblioteca "time" para o final do programa

valor1 = int(input('\nPrimeiro valor: '))          # Aqui recebe os valores
valor2 = int(input('Segundo valor: '))
opção = 0                                   # Aqui "opção" é inicializada com 0 para o laço "while" poder rodar diferente de 5

while opção != 5:                           # Enquanto "opção" for diferente de 5, o laço roda
    print('''\n[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')

    opção = int(input('\nQual sua escolha? '))      # Aqui "opção" sai de 0 e recebe um valor do usuário

    if opção == 1:          # Se "opção" for 1, soma os dois números
        print('\nA soma entre {} + {} é: {}'.format(valor1, valor2, valor1 + valor2))

    elif opção == 2:        # Se "opção" for 2, multiplica os dois números
        print('\nA multiplição de {} x {} é: {}'.format(valor1, valor2, valor1 * valor2))

    elif opção == 3:        # Se "opção" for 3, indica qual número é o maior ou se são iguais
        if valor1 > valor2:
            print('\n{} é maior que {}'.format(valor1, valor2))
        if valor2 > valor1:
            print('\n{} é maior que {}'.format(valor2, valor1))
        if valor1 == valor2:
            print('Ambos são iguais')

    elif opção == 4:        # Se "opção" for 4, o laço pede novamente dois números para o usuário e roda o menu de opções
        valor1 = int(input('\nPrimeiro valor: '))
        valor2 = int(input('Segundo valor: '))

    elif opção == 5:        # Se "opção" for 5, ele mostra essa mensagem com 2 segundos de pausa e encerra o programa
        print('\nFINALIZANDO...')

    else:       # Se "opção" for 0 ou acima de 5, ele mostra uma mensagem de erro e o laço roda novamente
        print('\nOpção inválida! Tente novamente.')

    print('=-=' * 15)
sleep(2)
print('\nPrograma finalizado!')
