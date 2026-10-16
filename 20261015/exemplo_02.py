idades=[33]
while True: #Controla entrada de dados
    while True: # controla ERRO (try)
        try:
            idade=int(input('Digite Idade [Zero encerra]:'))
            if idade == 0:
                break
            idades.append(idade)
            break
        except:
            print('Erro Digitação')
    if idade == 0:
        break
for i in range(len(idades)):
    print(f'{i}: {idades[i]}')
soma=sum(idades)
media=soma/len(idades)
print(f'Media de idade dos alunos{media:.2f}')