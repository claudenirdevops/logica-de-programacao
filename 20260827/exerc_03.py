# Exercício 3: Sistema de Aprovação Simples
# Desenvolva um programa para a secretaria acadêmica que solicite as notas de duas avaliações de um
# estudante. O programa deve calcular a média aritmética simples das duas notas:
# ● Se a média for 7.0 ou superior, exiba: "Média: [valor] - Aluno APROVADO!"
# ● Se a média for menor que 7.0, exiba: "Média: [valor] - Aluno em RECUPERAÇÃO."
# ● Conceitos: conversão para float(), cálculo de média, operadores aritméticos (+, /), estrutura if/else.

nota1 = float(input('Digite a nota (1ª): '))
nota2 = float(input('Digite a nota (2ª): '))

mas = (nota1 + nota2) / 2

if mas >= 7.0:
    mensagem = f'Média: {mas: .2f} - Aluno APROVADO!'
else:
    mensagem = f'Média: {mas: .2f} - Aluno em RECUPERAÇÃO.'

print(mensagem)