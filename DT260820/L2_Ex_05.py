# Exercício 5: Cálculo da área de um triângulo
# Crie um programa que calcule a área de uma figura triangular. O programa deve solicitar a medida da base e a medida da altura (em centímetros). Em seguida, calcule a área utilizando a fórmula matemática e mostre na tela o resultado: A área do triângulo é: [resultado] cm².
# Fórmula: $\text{Área} = \frac{\text{base} \times \text{altura}}{2}$
# Conceitos: input(), conversão para float(), operadores aritméticos (*, /), parênteses para precedência, print().

b = int(input("Informe a medida da base: "))
h = int(input("Informe a medida da altura: "))

resultado = (b * h)/2

print(f"A área do triângulo é: {resultado} cm².")