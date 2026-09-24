# Exercício 2: Somador de Gastos (Acumulador)
# Objetivo: Utilizar um laço com sentinela para acumular valores decimais até o usuário
# decidir parar.
# Enunciado: Desenvolva um script para somar os gastos de uma cozinha. O programa
# deve solicitar repetidamente que o usuário digite o valor de um item (float). A repetição
# deve continuar enquanto o valor digitado for diferente de 0. Quando o usuário digitar 0,
# encerre o laço e mostre o valor total acumulado das compras com duas casas decimais.

gastos = 0

valor = float(input('Digite o valor gasto: '))

while valor > 0 :
    gastos += valor
    print(gastos)
    valor = float(input('Digite o valor gasto ou zero para para encerrar: '))

print(f'\nGastos Totais: {gastos}')