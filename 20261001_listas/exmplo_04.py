from cores import RESET, BOLD, AZUL, VERMELHO, AMARELO

frutas=['Maça','Banana','Mamão']
print(frutas)
# método append => adiciona UM elemento no final da lista
frutas.append('Melão')
frutas.append('Kiwi')
frutas.append(50.43)
print(frutas)


while True:
    fruta=input(f'Digite uma Fruta {AZUL} [FIM]➡️Encerra:{RESET}')
    if fruta.upper() == 'FIM':
        break
    frutas.append(fruta)
qtd=len(frutas) # Calcula Quantidade de Elementos # frutas
print(f'Quantidade de elementos {qtd}')
for i in range(qtd):
    print(f'Índice{AZUL}🟰{RESET}{i} ➡️{frutas[i]} ')