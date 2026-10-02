frutas = []

while True:
    fruta = input('Digite uma Fruta [FIM] ==> Enecerra: ')
    if fruta.upper() == 'FIM':
        break
    frutas.append(fruta)

qtd = len(frutas)

print(f'Quantidade de elementos: {qtd}')

for i in range (qtd):
    print(f'{frutas[i]}')