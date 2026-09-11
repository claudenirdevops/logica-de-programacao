# Exercício 7: Somatório Sequencial
# Crie um programa que calcule e exiba a soma de todos os números inteiros existentes no
# intervalo de 1 a 100 ($1 + 2 + 3 + \dots + 100$). Mostre apenas o resultado final acumulado.
# Conceito trabalhado: Padrão de acumulador com inicialização fora do laço (soma = 0)

soma = 0

for i in range(1, 101):
    soma += i

print('Resultado final acumulado: ', soma)