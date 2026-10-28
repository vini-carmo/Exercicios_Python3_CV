total = maisdemil = contador = barato = 0               # inicializo as variáveis com 0 para contabilizar no final do programa
nomebarato = ' '                            # Inicio essa variável com string vazia pois ela vai receber o nome do produto mais barato ao final do programa

print('=' * 35)
print('         MERCADO CARMO')
print('=' * 35)

while True:     # Looping infinito para "while" rodar sem a necessidade de condição
    produto = str(input('\nNome do produto: ')).strip().title()        # Variável "produto" recebe o nome do produto digitado pelo usuário
    preço = float(input('Preço do produto: R$'))                       # Variável "preço" recebe o preço do produto digitado pelo usuário
    decisao = ' '                                   # Variável "decisão" recebe string vazia pois vai receber 'S' ou 'N'
    total = total + preço               # Variável "total" é somada com ela mesmo + "preço" a cada vez que o looping roda, para mostrar a soma do total gasto na compra
    contador = contador + 1             # Variável "contador" é somada de 1 em 1 para sabermos se o programa terá 1 ou mais produtos digitados

    if contador == 1 or preço < barato:     # Se tiver 1 produto digitado ou o preeço for o menor digitado, "nomebarato" recebe o nome do produto mais barato digitado
        barato = preço
        nomebarato = produto

    if preço > 1000:        # Se for digitado um preço maior que 1.000, "maisdemil" conta quantos produtos foram digitados nesse valor
        maisdemil = maisdemil + 1

    while decisao not in 'SN':
        decisao = str(input('Deseja cadastrar mais? [S/N] ')).strip().upper()[0]            # Aqui "decisao" recebe 'S' ou 'N'
        print('-' * 35)
    if decisao == 'N':      # Se "decisao" for 'N', função "break" encerra o programa e mostra os dados contabilizados pelas variáveis
        break

print(f'\nTotal gasto na compra: R${total:.2f}')
print(f'Produtos que custam mais de R$ 1.000,00: {maisdemil}')
print(f'Produto mais barato da compra: {nomebarato}')
