produtos=['mouse','Teclado']
quantidades=[10,11]
precos=[50,76]
def menu():
    print('--------------- MENU --------------')
    print('1 - Cadastrar Produtos')
    print('2 - Listar Estoque')
    print('9 - Fim')
    while True:
        try:
            opcao=int(input('Opção:'))
            break
        except:
            print('Opcção deve ser INT')
    return opcao
def cadastrar():
    while True:
        produto=input('Produto [FIM] encerra:')
        if produto.upper()=='FIM':
            break
        produtos.append(produto)
        while True:
            try:
                qtd=int(input('Quantidade:'))
                preco=float(input('Preço:'))
                quantidades.append(qtd)
                precos.append(preco)
                break
            except:
                print('Tente Novamente INT e FLOAT')

def listar():
    print('Produtos            | Quantidade |       Preço|       Total|')
    qtdTot=0
    totalEstoque=0
    for prod,qtd,preco in zip(produtos,quantidades,precos):
        print(f'{prod:<20}|{qtd:>12}|{preco:>12}|{qtd*preco:>12}')
        qtdTot+=qtd
        totalEstoque+=qtd*preco
    print(f'                     Tot Qtd = {qtdTot}        Total Valor = {totalEstoque}')

while True:
    opcao=menu()
    if opcao == 9:
        break
    elif opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    else:
        print('Opcao inválida')

print('Tchau - Fim do Programa')