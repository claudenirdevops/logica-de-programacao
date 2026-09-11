# Exercício 8: Tabuada Dinâmica
# Solicite que o usuário digite um número inteiro qualquer. Utilizando um laço for de 1 a 10,
# calcule e exiba a tabuada completa desse número no formato: X x Y = Z.
# Conceito trabalhado: Leitura com input(), range(1, 11) e formatação com f-strings.
# Nível 5: Integração com Condicionais e Entradas Múltiplas

num = int(input('Digite um número inteiro: '))

for i in range(1,11):
    print(f'{num} x {i} = {num*i}')