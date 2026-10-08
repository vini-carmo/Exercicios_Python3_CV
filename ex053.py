frase = str(input('\nDigite uma frase: ')).strip().upper()     # Pegou a frase, eliminou os espaços excedentes e colocou tudo em maiúsculo
palavras = frase.split()                                       # Gerou lista com .split() separando a frase
junto = ''.join(palavras)                                      # Juntou tudo numa string só com .join()
inverso = junto[::-1]                                          # Aqui inverteu a frase ao contrário
print('\nO inverso de {} é {}'.format(junto, inverso))
if inverso == junto:                                           # Aqui verifica a existência do PALÍNDROMO
    print('\nTemos um PALÍNDROMO!')
else:
    print('\nA frase NÂO é um PALÍNDROMO!')
