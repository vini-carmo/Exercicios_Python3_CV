sexo = str(input('\nInforme seu sexo [M/F]: ')).strip().upper()        # Variável "sexo" recebe um input str, sendo tranformado em maiúsculo e sem os espaços excedentes
while sexo not in 'M F':                                               # Enquanto em "sexo" não for digitado M ou F, o programa vai pedir novamente o sexo pro usuário
    sexo = str(input('Dados inválidos! Por favor, informe seu sexo: ')).strip().upper()
if sexo == 'M':                                                        # Se em "sexo" for digitado M, programa finaliza com mensagem
    print('\nSexo MASCULINO registrado com sucesso!')
if sexo == 'F':                                                        # Se em "sexo" for digitado F, programa finaliza com mensagem
    print('\nSexo FEMININO registrado com sucesso!')
