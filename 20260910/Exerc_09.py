# Exercício 9: Filtro de Múltiplos com Condicional
# Construa um algoritmo que percorra os números inteiros de 1 a 30. Para cada volta do laço,
# teste se o número é divisível por 3 (resto da divisão % 3 == 0). Se for divisível, exiba o número
# acompanhado da mensagem "-> Múltiplo de 3".
# Conceito trabalhado: Operador aritmético de módulo (%) integrado à estrutura de decisão dentro do corpo do laço.

for i in range(1,31):
    if i%3 == 0:
        print(f'Múltiplo de 3: {i}')
