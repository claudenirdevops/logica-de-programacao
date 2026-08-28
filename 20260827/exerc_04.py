# Exercício 4: Comparador de Dois Valores
# Faça um programa que solicite a entrada de dois números inteiros distintos. O algoritmo deve comparar
# os dois valores e informar qual deles é o maior no formato:
# ● "O primeiro número ([valor1]) é maior que o segundo ([valor2])."
# ● Caso contrário: "O segundo número ([valor2]) é maior que o primeiro ([valor1])."
# ● Conceitos: leitura de múltiplas variáveis, operador de comparação >, estrutura if/else, formatação com f-strings

print('DIGITE 2 (DOIS) NÚMEROS DISTINTOS:')

n1 = int(input('Digite um número (1º): '))
n2 = int(input('Digite um número (2º): '))

if n1 > n2:
    mensagem = f"O primeiro número {n1} é maior que o segundo {n2})."
else:
    mensagem = f"O segundo número {n2} é maior que o primeiro {n1})."

print(mensagem)