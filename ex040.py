print('\nVamos calcular a média das suas notas, lembrando que abaixo de 5 é REPROVAÇÃO e entre 5 e 6.9 é RECUPERAÇÃO!')
n1 = float(input('\nDigite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('\nSua média é {:.1f}, portanto você está REPROVADO!'.format(media))
elif 7 > media >= 5:
    print('\nSua média é {:.1f}, você está de RECUPERAÇÂO!'.format(media))
else:
    print('\nSua média é {:.1f}, você está APROVADO!'.format(media))
