# Exercício 1: Contagem Regressiva Simples (Contador)
# Objetivo: Praticar a inicialização, a condição de parada e o decremento de uma variável.
# Enunciado: Crie um programa que inicialize uma variável com o valor 10. Utilizando a
# estrutura while, exiba os números de 10 até 1 em ordem decrescente. Ao final do laço,
# exiba a mensagem: "Decolagem autorizada!".

contador = 10

while contador>0:
    print(contador)
    contador-=1

print('Decolagem autorizada!')