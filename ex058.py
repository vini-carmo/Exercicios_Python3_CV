from random import randint             # Aqui foi importado a função "randint" da bilbioteca "random", onde "randint" escolhe um número aleatório

computador = randint(0, 10)            # Aqui "randint" vai escolher um número entre 0 e 10
tentativas = 0                   # Inicializada a variável "tentativas" com o valor 1, para contabilizar quantas tentativas o usuário precisou para vencer o computador
acertou = False                  # Essa variável "acertou" está com o valor False para enquanto o usuário NÃO acertar o mesmo número do computador

print('\nVou pensar em um número entre 0 e 10, tente adivinhar...')

while not acertou:
    usuario = int(input('Em que número eu pensei? '))          # Aqui a variável "usuario" recebe o número que o usuário acha que foi o mesmo do computador
    tentativas += 1                                     # Aqui "tentativas" fica contabilizando de 1 em 1 a cada erro do usuário
    if  usuario == computador:                          # Se "usuario" for igual "computador", o valor da variável "acertou" vira True
        acertou = True
    else:
        if computador > usuario:                  # Se o número do computador for maior que o do usuário, mostra uma mensagem dizendo que o número é maior
            print('Mais... Tente acertar novamente: ')
        else:                                     # Se o número do computador for menor que o do usuário, mostra uma mensagem dizendo que o número é menor
            print('Menos... Tente acertar novamente: ')
print('\nVOCÊ ACERTOU! Precisou de {} tentativas para acertar o número {}'.format(tentativas, computador))
