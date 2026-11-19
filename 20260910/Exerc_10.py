# Exercício 10: Média de Gastos com Repetição Pré-definida
# Desenvolva um programa para controle financeiro semanal. O laço for deve rodar exatamente
# 5 vezes (representando os 5 dias úteis). A cada repetição, o programa deve solicitar o valor
# gasto no dia (via input()) e somar esse valor a uma variável acumuladora. Ao término das 5
# iterações, o programa deve exibir:
# 1. O valor total gasto na semana.
# 2. A média diária de gastos.
# ● Conceito trabalhado: input() sucessivo dentro do laço, conversão para float, totalização
# e cálculo de média após o encerramento do for.

soma = 0

for i in range(1,6):
    valor = float(input('Digite o valor gasto no dia: '))
    soma += valor

print(f'O valor gasto na semana: {soma}')
print(f'A media de gastos: {soma/5}')