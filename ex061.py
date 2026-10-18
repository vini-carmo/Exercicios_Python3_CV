print('\n{:=^40}'.format(' 10 TERMOS DE UMA PA '))
primeiro = int(input('\nPrimeiro termo: '))         # Aqui "primeiro" recebe o número que inicará a progressão aritmética
razao = int(input('Razão da PA: '))                 # Aqui "razao" recebe o número que contará de tanto em tanto na progressão

termo = primeiro        # Aqui "termo" recebe o valor de "primeiro" para somar com "razao" no laço e assim fazer a progressão
contador = 1            # Aqui "contador" recebe o valor 1 para o laço while rodar até 10

while contador <= 10:
    print('{} - '.format(termo), end='')
    termo = termo + razao       # Aqui "termo" é somado com "razao" até chegar no décimo número somado
    contador = contador + 1     # Aqui "contador" recebe ele mesmo + 1 para o programa parar na décima repetição
print('FIM')
