num = int(input('\nDigite um número inteiro: '))

print('''\nEscolha uma das bases para conversão:
\n[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opção = int(input('\nSua opção: '))

if opção == 1:
    print('\n{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))

elif opção == 2:
    print('\n{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))

elif opção == 3:
    print('\n{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

else:
    print('\nOpção inválida! Você só pode escolher entre 1 e 3.')
