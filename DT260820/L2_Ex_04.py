# Exercício 4: Calculando a idade a partir do ano de nascimento
# Faça um programa que pergunte o nome do usuário, o ano atual (ex: 2026) e o ano em que ele nasceu. O programa deve calcular a idade aproximada subtraindo o ano de nascimento do ano atual e exibir a mensagem: Olá, [Nome]! Você tem aproximadamente [idade] anos.
# Conceitos: manipulação de texto (str), conversão numérica (int), operador de subtração (-), concatenação ou f-string no print().

nome = input("Informe o seu nome: ")
ano = int(input("Informe o ano atual: "))
dn_ano = int(input("Informe o ano de nascimento: "))

idade = ano - dn_ano

print(f"Olá, {nome}! Você tem aproximadamente {idade} anos.")