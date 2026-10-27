mais18 = homens = mulheres20 = 0        # inicializo as variáveis com 0 para contabilizar no final do programa

print('=' * 35)
print('        CADASTRO DE PESSOA')
print('=' * 35)

while True:     # Looping infinito para "while" rodar sem a necessidade de condição
    i = int(input('\nIdade: '))         # Variável "i" recebe a idade do usuário
    s = ' '                             # Variável "s" inicializada com string vazia para while poder rodar e depois "s" receber 'M' ou 'F'

    while s not in 'MF':
        s = str(input('Sexo: [M/F] ')).strip().upper()[0]           # Aqui "s" recebe 'M' ou 'F'
        print('-' * 35)
    decisao = ' '                       # Variável "decisao" inicializada com string vazia para while poder rodar e depois "decisao" receber 'S' ou 'N'
    if i > 18:               # Esses IFs contabilizam as variáveis iniciadas em 0 se as condições forem digitadas pelo usuário
        mais18 += 1
    if s == 'M':
        homens += 1
    if s == 'F' and i < 20:
        mulheres20 += 1

    while decisao not in 'SN':
        decisao = str(input('Deseja cadastrar mais? [S/N] ')).strip().upper()[0]            # Aqui "decisao" recebe 'S' ou 'N'
        print('-' * 35)
    if decisao == 'N':      # Se "decisao" for 'N', função "break" encerra o programa e mostra os dados contabilizados pelas variáveis
        break

print(f'\nPessoas com mais de 18 anos: {mais18}')
print(f'Homens registrados: {homens}')
print(f'Mulheres com menos de 20 anos: {mulheres20}')
