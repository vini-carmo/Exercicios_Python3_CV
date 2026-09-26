from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) # Aqui vai escolher um número entre 0, 1 e 2

print('''\nSuas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('\nQual é sua escolha? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('\nEu escolhi: {}'.format(itens[computador])) # Aqui vai substituir 0, 1 e 2 por PEDRA, PAPEL, TESOURA
print('\nVocê escolheu: {}'.format(itens[jogador]))

if computador == 0:
    if jogador == 0:
        print('\nEMPATE')
    elif jogador == 1:
        print('\nVocê GANHOU!')
    elif jogador == 2:
        print('\nVocê PERDEU!')
    else:
        print('\nOpção inválida!')

elif computador == 1:
    if jogador == 0:
        print('\nVocê PERDEU!')
    elif jogador == 1:
        print('\nEMPATE')
    elif jogador == 2:
        print('\nVocê GANHOU!')
    else:
        print('\nOpção inválida!')

elif computador == 2:
    if jogador == 0:
        print('\nVocê GANHOU!')
    elif jogador == 1:
        print('\nVocê PERDEU!')
    elif jogador == 2:
        print('\nEMPATE')
    else:
        print('\nOpção inválida!')
