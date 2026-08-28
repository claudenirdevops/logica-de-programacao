# Exercício 2: Número Par ou Ímpar
# Escreva um programa que peça ao usuário para digitar um número inteiro. Utilizando o operador de
# resto da divisão (%), determine se o número é par ou ímpar e exiba o resultado correspondente:
# ● Se o resto da divisão por 2 for zero: "O número é PAR."
# ● Caso contrário: "O número é ÍMPAR."
# ● Conceitos: int(), operador módulo (%), operador de igualdade (==), estrutura if/else

n = int(input('Digite um numero: '))

if n%2 == 0:
    mensagem = 'O número é par!'
else:
    mensagem = 'O número é impar!'

print(mensagem)