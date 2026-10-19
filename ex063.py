print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

n = int(input('\nQuantos termos deseja mostrar? '))     # Aqui "n" recebe a quantidade de termos que a sequência terá
t1 = 0                                                  # Aqui, "t1" recebe 0 pois a sequência sempre começa em 0
t2 = 1                                                  # Aqui, "t2" recebe 1 pois após o 0 da sequência sempre vêm o 1
print('~' * 50)
print('{} - {}'.format(t1, t2), end=' ')        # Aqui é printado o começo da sequência (0, 1), estabelecendo sua estrutura e como ela funcionará
contador = 3                                    # O "contador" começa em 3 pois os 2 primeiros números da sequência já foram estabelecidos
while contador <= n:                       # Se o contador for maior que 3, o programa roda quantas vezes foram digitadas em "n"
    t3 = t1 + t2                           # Aqui "t3" recebe a soma de 0 (t1) + 1 (t2), que é 1
    print('- {}'.format(t3), end=' ')
    contador = contador + 1             # Aqui "contador" recebe ele mesmo (3) + 1 para poder parar o laço quando chegar no número digitado em "n"
    t1 = t2                       # Para os dois números anteriores serem somados e "t3" sempre ter um novo número, "t1" passa a ocupar o lugar de "t2" e "t2" de "t3"
    t2 = t3                       # Assim o laço vai rodar até a quantidade digitada em "n"
print('- FIM')
