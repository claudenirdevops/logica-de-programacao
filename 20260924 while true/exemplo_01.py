idade = 0
soma = 0
cont = 1
idade = int(input('Digite a idade do aluno: '))
while idade >= 0:
    soma += idade
    cont += 1
    while True:
        try:
            idade = int(input('Digite a idade do aluno:'))
            break
        except:
            print("CRIATURA você digitou ERRADO")
            print("DIGITE somente INTEIROS")

print(f'media das idades:{(soma/cont):.2f}')