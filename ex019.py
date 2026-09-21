from random import choice
a1 = str(input('Primeiro aluno(a): '))
a2 = str(input('Segundo aluno(a): '))
a3 = str(input('Terceiro aluno(a): '))
a4 = str(input('Quarto aluno(a): '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('\nO aluno(a) escolhido(a) foi: {}!'.format(escolhido))
