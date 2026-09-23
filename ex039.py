from datetime import date

nascimento = int(input('\nAno de nascimento: '))
atual = date.today().year
idade =  atual - nascimento
sexo = str(input('\nVocê é homem ou mulher? ')).strip().title()
print('\nQuem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))

if sexo == 'Homem' and idade > 18:
    print('\nJá se passaram {} ano(s) do seu alistamento, que foi em {}!'.format(idade - 18, nascimento + 18))
elif sexo == 'Homem' and idade == 18:
    print('\nVocê está no seu ano de alistamento ({})! Se aliste já no site do governo.'.format(atual))
elif sexo == 'Homem' and idade < 18:
    print('\nVocê deve se alistar no ano que completa 18, em {}.\n\nAinda faltam {} ano(s)!'.format(nascimento + 18, 18 - idade))
elif sexo == 'Mulher':
    print('\nVocê é mulher, no Brasil não é obrigatório seu alistamento!')
