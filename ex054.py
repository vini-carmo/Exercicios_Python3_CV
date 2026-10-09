from datetime import date                                       # Importa a função Date da biblioteca Datetime, que mostra o ano atual do computador
atual = date.today().year
maioridade = 0
menoridade = 0
for pessoas in range(1, 8):                                     # Pergunta 7x o ano de nascimento das pessoas e recebe esses anos
    nasc = int(input('Em que ano a {}a pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc                                        # Calcula se a pessoa é maior de idade ou não, baseado no ano atual do computador
    if idade >= 18:
        maioridade += 1                                         # Se as pessoas forem +18, essa variável vai receber quantas pessoas são maior de idade
    else:
        menoridade += 1                                         # Se as pessoas forem -18, essa variável vai receber quantas pessoas são menores de idade
print('\nAo todo, tivemos {} pessoas maiores de idade e {} pessoas menores de idade.'.format(maioridade, menoridade))
