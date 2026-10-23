c = s = 0       # Aqui inicializo as variáveis de contador e somador com 0

while True:     # Aqui é um comando para o laço while rodar independente de condição alguma (enquanto for verdadeiro, execute tal ação)
    n = int(input('Digite um número (999 para parar): '))        # Variável "n" recebe o número inteiro digitado pelo usuário
    if n == 999:     # Se em "n" for digitado 999, função break encerra o programa e mostra no final a soma de todos os x números digitados sem contar a flag 999
        break
    s += n      # Essa estrutura soma todos os números digitados pelo usuário, e está após o break para NÃO somar o flag 999
    c += 1      # Essa estrutura conta quantos números foram digitados pelo usuário, e está após o break para NÃO contar o flag 999
print(f'\nA soma dos {c} números digitados foi {s}')
