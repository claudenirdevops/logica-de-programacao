# Exercício 6: Inspetor e Contador de Espaços
# Escreva um programa que receba uma frase digitada pelo usuário. Utilizando uma estrutura for
# combinada com if e uma variável contadora, conte quantos espaços em branco (" ") existem na
# frase e imprima o total apurado ao final.
# Conceito trabalhado: for sobre str, contador numérico e condicional simples.
# Nível 4: Acumuladores e Cálculos Matemáticos

frase = input("Digite uma frase: ")

contador = 0

for i in range(len(frase)):
    if frase[i] == " ":
        contador += 1

print(f"Total de espaços encontrados: {contador}")