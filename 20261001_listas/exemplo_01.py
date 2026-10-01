frutas = ['Maça', 'Banana', 'Mamão']
print(frutas)

frutas.append('Abacaxi')
print(frutas)

qtd = len(frutas)

print(f'Quantidade de elementos: {qtd}')

for i in range (qtd):
    print(f'Índice = {i} => {frutas[i]}')