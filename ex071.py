print('=' * 35)
print('{:^35}'.format('BANCO CARMO'))
print('=' * 35)

valor = int(input('\nQual valor você quer sacar? R$ '))     # Aqui "valor" recebe o valor inteiro que o usuário deseja sacar no caixa
total = valor       # "total" recebe o valor de "valor"
ced = 50            # "ced" recebe 50 que é a cédula mais alta do caixa
totalced = 0        # "totalced" recebe 0 para contabilizar quantas cédulas de cada valor precisa para sacar o valor

while True:                 # Looping infinito para "while" rodar sem a necessidade de condição
    if total >= ced:        # Se o valor do usuário for maior ou igual a 50, então será retirado 50 do valor digitado pelo usuário
        total = total - ced
        totalced = totalced + 1     # Aqui "totalced" é somado de 1 em 1 para termos quantas cédulas de cada valor será necessário
    else:
        if totalced > 0:        # Se um determinado valor não precisar de nenhuma cédula, o programa não escreve nada pro usuário
            print(f'Total de {totalced} cédulas de {ced} reais')
        if ced == 50:       # Aqui essa estrutura vai diminuindo e contabilizando as cédulas para 50, 20, 10 e 1
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:      # Quando as cédulas acabarem com o valor, o programa se encerra
            break
print('=' * 35)
print('\nObrigado por sacar, volte sempre!')
