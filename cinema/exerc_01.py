# Listas iniciais
filmes = ['Avatar', 'Batman']
ingressos = [50, 30]
precos = [35.0, 30.0]

def listar_catalogo():
    print("\n" + "=" * 60)
    print(f"{'FILME':20} {'INGRESSOS':10} {'PREÇO':10} {'TOTAL(R$)':10}")
    print("=" * 60)

    total_ingressos = 0
    total_caixa = 0

    for i in range(len(filmes)):
        total_filme = ingressos[i] * precos[i]
        total_ingressos += ingressos[i]
        total_caixa += total_filme

        print(f"{filmes[i]:20} {ingressos[i]:10} {precos[i]:10.2f} {total_filme:10.2f}")

    print("=" * 60)
    print(f"Total de ingressos: {total_ingressos}")
    print(f"Valor potencial do caixa: R$ {total_caixa:.2f}")
    print("=" * 60)


def cadastrar_filmes():
    while True:
        titulo = input("\nDigite o nome do filme (FIM para encerrar): ")

        if titulo.upper() == "FIM":
            break

        try:
            qtd = int(input("Quantidade de ingressos: "))
            preco = float(input("Preço do ingresso: R$ "))
        except ValueError:
            print("Erro: digite valores numéricos válidos.")
            continue

        filmes.append(titulo)
        ingressos.append(qtd)
        precos.append(preco)

        print("Filme cadastrado com sucesso!")


def vender_ingressos():
    listar_catalogo()

    titulo = input("\nDigite o nome do filme: ")

    if titulo in filmes:
        pos = filmes.index(titulo)

        try:
            qtd = int(input("Quantidade de ingressos: "))
        except ValueError:
            print("Quantidade inválida.")
            return

        if qtd <= ingressos[pos]:
            ingressos[pos] -= qtd
            print("Venda realizada com sucesso!")
        else:
            print("Ingressos insuficientes.")
    else:
        print("Filme não encontrado.")


def repor_ingressos():
    listar_catalogo()

    titulo = input("\nDigite o nome do filme: ")

    if titulo in filmes:
        pos = filmes.index(titulo)

        try:
            qtd = int(input("Quantidade a repor: "))
        except ValueError:
            print("Quantidade inválida.")
            return

        ingressos[pos] += qtd
        print("Reposição realizada com sucesso!")
    else:
        print("Filme não encontrado.")


def excluir_filme():
    listar_catalogo()

    titulo = input("\nDigite o nome do filme a excluir: ")

    if titulo in filmes:
        pos = filmes.index(titulo)

        del filmes[pos]
        del ingressos[pos]
        del precos[pos]

        print("Filme excluído com sucesso!")
    else:
        print("Filme não encontrado.")


# Programa principal
while True:
    print("\n===== CINEMA =====")
    print("1 - Cadastrar Filmes")
    print("2 - Listar Catálogo")
    print("3 - Vender Ingressos")
    print("4 - Repor Ingressos")
    print("5 - Excluir Filme")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_filmes()
    elif opcao == "2":
        listar_catalogo()
    elif opcao == "3":
        vender_ingressos()
    elif opcao == "4":
        repor_ingressos()
    elif opcao == "5":
        excluir_filme()
    elif opcao == "6":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida!")