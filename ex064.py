n = contador = soma = 0                                     # Inicializei as variáveis com o valor 0
n = int(input('Digite um número [999 para parar]: '))       # "n" recebe o valor digitado pelo usuário, se for 999 o programa já não roda

while n != 999:             # Enquanto "n" for diferente de 999, o laço roda com "contador" contando de 1 em 1 e somando apenas os números que não forem 999 em "soma"
    contador = contador + 1
    soma = soma + n
    n = int(input('Digite um número [999 para parar]: '))

print('\nVocê digitou {} números e a soma entre eles foi {}'.format(contador, soma))  # Aqui ele fala quantos números foram digitados (sem contar o 999) e a soma deles
