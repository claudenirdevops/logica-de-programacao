# Exercício 3: Cálculo da área de um retângulo
# Escreva um programa que calcule a área de um terreno retangular. O usuário deve informar a largura (em metros) e o comprimento (em metros). O programa deve multiplicar esses dois valores para encontrar a área total e exibir: A área total do terreno é: [resultado] metros quadrados.
# Fórmula: $\text{Área} = \text{largura} \times \text{comprimento}$
# Conceitos: input(), conversão para float(), operador de multiplicação (*), print().

largura = int(input("Informe a largura do terreno retangular em metros: "))
comprimento = int(input("Informe o comprimento do terreno retangular em metros: "))

resultado = largura * comprimento

print(f"A área total do terreno é: {resultado} metros quadrados.")