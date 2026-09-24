from datetime import date

ano = int(input('\nAno de nascimento: '))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    print('\nVocê tem {} anos, então é MIRIM!'.format(idade))
elif idade <= 14:
    print('\nVocê tem {} anos, então é INFANTIL!'.format(idade))
elif idade <= 19:
    print('\nVocê tem {} anos, então é JÙNIOR!'.format(idade))
elif idade <= 25:
    print('\nVocê tem {} anos, então é SÊNIOR!'.format(idade))
else:
    print('\nVocê tem {} anos, então é MASTER!'.format(idade))
