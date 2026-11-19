# Exercício Prático: Sistema de Controle de Ingressos de Cinema
# Enunciado: Desenvolva um programa em Python estruturado com funções e listas paralelas para gerenciar a bilheteria e a disponibilidade de ingressos de uma rede de cinemas.
#
# O programa deve iniciar com três listas predefinidas:
#
# filmes = ['Avatar', 'Batman']
#
# ingressos = [50, 30]
#
# precos = [35.0, 30.0]
#
# Requisitos e Funcionalidades:
# O sistema deve apresentar um menu principal em um laço de repetição contínuo com as seguintes opções:
#
# Cadastrar Filmes: Permite adicionar novos filmes informando o título (com a palavra 'FIM' para encerrar o cadastro), a quantidade inicial de ingressos disponíveis (int) e o preço do ingresso (float). Utilize tratamento de erros (try/except) para garantir que os valores numéricos sejam digitados corretamente.
#
# Listar Catálogo: Exibe uma tabela formatada contendo o nome do filme, a quantidade de ingressos disponíveis, o preço unitário e o valor total arrecadado caso todos os ingressos disponíveis sejam vendidos. Ao final, mostre o somatório da quantidade total de ingressos e o valor potencial do caixa.
#
# Vender Ingressos: Lista o catálogo, solicita o nome do filme que o cliente deseja assistir e a quantidade de ingressos a ser comprada, subtraindo essa quantidade do estoque correspondente.
#
# Repor Ingressos: Lista o catálogo, solicita o nome do filme e a quantidade de novos ingressos recebidos, somando-os ao estoque atual.
#
# Excluir Filme: Lista o catálogo, solicita o nome do filme a ser removido e apaga os dados correspondentes de todas as três listas paralelas, exibindo uma mensagem de sucesso.
#
# Sair (Fim): Encerra a execução do programa.

# 3 Listas predefinidas

filmes = ['Avatar', 'Batman']

ingressos = [50, 30]

precos = [35.0, 30.0]