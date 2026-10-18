print('\n{:=^40}'.format(' 10 TERMOS DE UMA PA '))
primeiro = int(input('\nPrimeiro termo: '))         # Aqui "primeiro" recebe o número que inicará a progressão aritmética
razao = int(input('Razão da PA: '))                 # Aqui "razao" recebe o número que contará de tanto em tanto na progressão

termo = primeiro        # Aqui "termo" recebe o valor de "primeiro" para somar com "razao" no laço e assim fazer a progressão
contador = 1            # Aqui "contador" recebe o valor 1 para o laço while rodar até 10
total = 0               # Variável "total" serve para contar quantos termos ao todo o programa irá mostrar
mais = 10               # Variável "mais" serve para guardar na memória do computador que o laço tem 10 repetições primeiro e o programa terá 10 termos

while mais != 0:        # Enquanto o programa tiver mais de 0 repetições, ele roda e "total" começa a contar quantos termos o programa vai ter
    total = total + mais
    while contador <= total:
        print('{} - '.format(termo), end='')
        termo = termo + razao       # Aqui "termo" é somado com "razao" até chegar no décimo número somado
        contador = contador + 1     # Aqui "contador" recebe ele mesmo + 1 para o programa parar na décima repetição
    print('PAUSA')
    mais = int(input('\nQuantos termos a mais deseja mostrar? '))       # Aqui se o usuário digitar 0, o programa termina, se não, roda novamente
print('\nFIM! A progressão teve ao todo {} termos.'.format(total))
