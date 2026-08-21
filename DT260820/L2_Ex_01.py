# Exercício 1: Somando dois números inteiros
# Desenvolva um programa que peça ao usuário para digitar dois números inteiros. O programa deve somar esses dois valores, armazenar o resultado em uma variável e exibir na tela a mensagem: A soma entre os dois números é: [resultado].
# Conceitos: input(), conversão para int(), operador de soma (+), print().

n1, n2 = map(int, input("Digite dois numeros inteiros separados por espaço: ").split())

resultado = n1 + n2

print(f"A soma entre os dois números é: {resultado}")