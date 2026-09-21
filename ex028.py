from random import randint
from time import sleep
computador = randint(0, 5)
print('\nVou pensar em um número entre 0 e 5, tente adivinhar...')
usuario = int(input('\nEm que número eu pensei? '))
print('\nPROCESSANDO...')
sleep(1)
if usuario == computador:
    print('\nVOCÊ GANHOU! Conseguiu adivinhar meu número!')
else:
    print('\nGANHEI! Pensei no número {} e não no {}!'.format(computador, usuario))
