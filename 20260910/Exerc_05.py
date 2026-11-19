# Exercício 5: Soletração Vertical de Palavra
# Peça para o usuário digitar uma palavra qualquer via teclado (input()). Utilizando o laço for,
# percorra essa palavra e imprima cada caractere isolado em uma linha diferente.
# Conceito trabalhado: Strings como sequências ordenadas de caracteres.

palavra = input('Digite uma palavra: ')

for i in range(len(palavra)):
    print(f'Indice {i}: {palavra[i]}')
