# Exercício 3: Contador de Números Pares (Contador + Condicional)
# Objetivo: Combinar estrutura de repetição com teste condicional simples (if).
# Enunciado: Escreva um programa que use um contador iniciando em 1 e indo até 20.
# Dentro do laço while, teste cada número: se o número for par (utilize o operador de resto % 2 == 0), exiba o número na tela

contador = 1

while contador <= 20 :
    if (contador%2 == 0):
        print(f'Este número é par: {contador}')
    contador += 1
