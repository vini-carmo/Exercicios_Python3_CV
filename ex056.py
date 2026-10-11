somaidade = 0                                               # Variável para somar todas as idades
media = 0                                                   # Variável para calcular a média das idades
maioridade = 0                                              # Variável para saber o homem mais velho
nomevelho = ''                                              # Variável para saber o nome do homem mais velho
mulhervinte = 0                                             # Variável para saber quantas mulheres tem menos de 20 anos

for p in range(1,5):                                        # Aqui recebe nome, idade e sexo de 4 pessoas
    print('----- {}a PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M | F): ')).strip().upper()
    somaidade = somaidade + idade                           # Aqui "somaidade" recebe a soma de todas as idades digitadas
    if p == 1 and sexo in 'M':                              # Se só tiver uma entrada de dados e o sexo for "M", naturalmente o homem mais velho vai ser esse
        maioridade = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridade:                  # Se o sexo for "M" e a "idade" for maior que a "maioridade", então "idade" passa a ser a maior e "nomevelho" passa a ser o nome do homem mais velho
        maioridade = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:                          # Se o sexo for "F" e a "idade" for menor que 20, "mulhervinte" irá receber a quantidade de mulheres com menos de 20 anos que foram digitadas
        mulhervinte = mulhervinte + 1
media = somaidade / 4                                       # Aqui calcula a média de idade (soma todas as idades em "somaidade" e divide por 4)

print('\nA média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulhervinte))
