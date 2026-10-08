print('\n{:=^40}'.format(' 10 TERMOS DE UMA PA '))
termo = int(input('\nPrimeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10-1) * razao
for c in range(termo,decimo + razao, razao):
    print(c, end=' - ')
print('FIM')
