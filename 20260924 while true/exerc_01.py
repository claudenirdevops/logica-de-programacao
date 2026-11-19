# ### 1. Sistema de Votação Simples
# Crie um programa que funcione como uma mini urna.
# O usuário deve digitar o número do candidato (1 para "Candidato A", 2 para "Candidato B") ou
# 0 para sair e encerrar a votação. Ao final, o programa deve mostrar quem ganhou ou se houve empate.

soma_A = 0
soma_B = 0
soma_nulos = 0

while True:
    while True:
        try:
            voto = int(input('Digite o número 1 para o candidato A ou 2 para o B. Para sair, digite zero (0): '))
        except:
            print('Digite somente volo com valor inteiro.')

    if voto == 1:
        soma_A += 1
    elif voto == 2:
        soma_B += 1
    elif voto == 0:
        break
    else:
        soma_nulos += 1


print(f'O total de votos: {soma_A} para o canditato A, {soma_B} para o candidato B e {soma_nulos} de votos nulos.')