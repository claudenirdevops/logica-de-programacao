# Validação de Entrada com Loop Infinito: Desenvolva um programa que solicite a idade de um usuário.
# Utilize um loop while True e um bloco try/except para garantir que o usuário digite apenas números inteiros.
# O programa deve continuar pedindo a entrada até que um valor válido seja fornecido e, ao final, exibir a idade aceita

while True:
  try:
    idade = int(input("Digite a sua idade: "))
    break  # Encerra o loop se a conversão para inteiro der certo
    except ValueError:
    print("Entrada inválida! Por favor, digite apenas números inteiros.")

print(f"Idade aceita: {idade} anos.")