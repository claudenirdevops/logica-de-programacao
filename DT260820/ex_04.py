# 4. ** Repetição de Frase **
# Pergunte ao usuário uma frase e quantas vezes ele gostaria de repetir. A seguir, imprima a frase o número de vezes solicitado.

frase = input("Digite um frase: ")
n = int(input("Informe quantas vezes essa frase será repetida: "))

resultado = (frase + '\n') * n

print('*'*50)
print(resultado)
print('*'*50)

print("Outra forma:")
print(f"{frase} \n" * n)