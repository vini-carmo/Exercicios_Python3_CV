from random import randint      # Aqui importo a função "randint" da biblioteca "random" para o computador escolher um número de 0 a 10

print('\nJOGO DO PAR OU ÍMPAR')
print('-' * 45)
v = 0       # Inicializo a variável "v" com 0 para contabilizar quantas vitórias consecutivas o usuário teve

while True:     # Estrutura de looping infinito para "while" rodar independente de condição alguma
    n = int(input('\nDigite um número: '))      # Variável "n" recebe o número que o usuário deseja jogar
    computador = randint(0, 10)                 # Variável "computador" recebe um número entre 0 e 10 que o computador escolher
    total = computador + n                      # Variável "total" recebe a soma dos dois números para depois sabermos se é par ou ímpar
    tipo = ' '                                  # Variável "tipo" recebe uma string vazia para depois receber 'P' ou 'I'

    while tipo not in 'PI':         # Como a variável "tipo" está vazia, então esse "while" roda normalmente
        tipo = str(input('Par ou Ímpar (P/I)? ')).strip().upper()[0]            # Variável "tipo" recebe do usuário se ele escolhe par (P) ou ímpar (I)
    print(f'\nVocê escolheu {n} e o computador {computador}, totalizando {total}.')     # Aqui mostra pro usuário a soma dos números

    if tipo == 'P':     # Se o usuário escolher par 'P', essa estrutura verifica se o total da soma dos dois números é par e diz se ele ganhou ou perdeu
        if total % 2 == 0:
            print(f'O número {total} é PAR, você VENCEU!')
            v = v + 1
        else:
            print(f'O número {total} é ÍMPAR, você PERDEU!')
            break

    elif tipo == 'I':   # Se o usuário escolher ímpar 'I', essa estrutura verifica se o total da soma dos dois números é ímpar e diz se ele ganhou ou perdeu
        if total % 2 != 0:
            print(f'O número {total} é ÍMPAR, você VENCEU!')
            v = v + 1
        else:
            print(f'O número {total} é PAR, você PERDEU!')
            break
                                                                                # Em "break", o laço para e o programa finaliza quando o usuário perde
    print('\nO jogo só para quando você perder, vamos jogar novamente...')
print(f'\nVocê venceu {v} vezes, programa FINALIZADO!')                         # O programa mostra quantas vezes seguidas o usuário ganhou do computador
