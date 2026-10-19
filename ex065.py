soma = contador = media = maior = menor = 0     # Inicio as variáveis com o valor inteiro 0
resp = 'S'                                      # Inicio "resp" com o valor string 'S' para o laço while poder rodar

while resp == 'S':
    n = int(input('Digite um número: '))        # Aqui "n" recebe o valor inteiro digitado pelo usuário
    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]        # Aqui se "resp" receber N, o laço para de rodar e o programa finaliza
    contador = contador + 1                     # Aqui "contador" recebe ele mesmo + 1 para contabilizar quantos valores foram digitados no laço
    soma = soma + n                             # Aqui "soma" recebe ela mesmo + "n" para somar todos os números do laço
    if contador == 1:                        # Se houver apenas 1 número digitado pelo usuário, automaticamente ele é o maior e o menor da sequência e "n" recebe ambos
        maior = menor = n
    else:               # Se houver mais que 1 número digitado, então essa estrutura designa "maior" para o maior número digitado, e "menor" para o menor número digitado
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = soma / contador     # Aqui "media" recebe a soma de todos os números do laço dividido pela quantidade de números digitados
print('\nA média entre todos os {} valores digitados foi {}'.format(contador, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
