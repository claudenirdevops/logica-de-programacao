# Exercício 1: Verificador de Maioridade
# Crie um programa que solicite a idade do usuário. O algoritmo deve verificar a idade informada: se for
# igual ou superior a 18 anos, exiba a mensagem "Você é maior de idade.". Caso contrário, exiba "Você é
# menor de idade.".
# ● Conceitos: input(), conversão para int(), estrutura if/else, operador >=.

idade = int(input('Digite a sua idade: '))

if idade >= 18:
    mensagem = 'Você é maior de idade'
else:
    mensagem = 'Você é menor de idade'

print(mensagem)

