lanches = ['coxinha', 'pastel']
quantidades = [12, 8]
precos = [7.50, 8.00]

def cadastrar_lAnche ()
    while True:
        nome_lanche.upper = input("\nDigite o nome do lanche (FIM para encerrar): ")

        if nome_lanche.upper() == "FIM":
            break

        try:
            qtd = int(input("Quantidade: "))
            preco = float(input("Preço do lanche: R$ "))
        except ValueError:
            print("Erro: digite valores numéricos válidos.")
            continue

        lanches.append(lanche)
        qtd.append(qtd)
        precos.append(preco)

        print("O lanche foi cadastrado com sucesso!")

def excluir_lanche():
    listar_estoque()

    nome_lanche.upper = input("\nDigite o nome do lanche a excluir: ")

    if nome_lanche in estoque:
        pos = lanches.index(nome_lanche)

        del nome_lanche[pos]
        del qtd[pos]
        del preco[pos]

        print("O lanche foi excluído com sucesso!")

    else:
        print("O lanche não foi encontrado!")
