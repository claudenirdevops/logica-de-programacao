produtos=['mouse','Teclado']
quantidades=[10,11]
precos=[50,76]

def menu():
    print('--------------- MENU --------------')
    print('1 - Cadastrar Produtos')
    print('2 - Listar Estoque')
    print('3 - Vender')
    print('4 - Comprar')
    print('5 - Excluir Produto')
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
def venda():
    listar()
    prod=input('Produto Vendido:')
    qtdVenda=int(input('Quantidade:'))
    indice=produtos.index(prod)
    quantidades[indice]-=qtdVenda
def comprar():
    listar()
    prod=input('Produto Comprado:')
    qtdComprada=int(input('Quantidade:'))
    indice=produtos.index(prod)
    quantidades[indice]+=qtdComprada
def excluir():
    listar()
    prod = input('Produto para Excluir:')
    indice=produtos.index(prod)
    del produtos[indice]
    del quantidades[indice]
    del precos[indice]
    print (f'Produto {prod} Excluído com SUCESSO!')
    input("[ENTER] para continuar")


# inicio Programa
while True:
    opcao=menu()
    if opcao == 9:
        break
    elif opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
        input('[ENTER] continua ...')
    elif opcao == 3:
        venda()
    elif opcao == 4:
        comprar()
    elif opcao == 5:
        excluir()
    else:
        print('Opcao inválida')

print('Tchau - Fim do Programa')