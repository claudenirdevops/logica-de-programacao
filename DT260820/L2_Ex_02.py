# Exercício 2: Calculando o troco (Subtração)
# Crie um programa para ajudar no caixa de uma lanchonete. O programa deve solicitar:
# O valor total da compra (ex: 35.00).
# O valor em dinheiro entregue pelo cliente (ex: 50.00).
# O programa deve calcular o valor do troco subtraindo o total da compra do valor pago e exibir o resultado com a mensagem: O troco do cliente é: R$ [valor].
# Conceitos: input(), conversão para float(), operador de subtração (-), print().

compras = float(input("Digite o valor total das compras: "))

recebimento = float(input("Digite o valor recebido pelo cliente: "))

valor = recebimento - compras

print(f"O troco do cliente é: R$ {valor}.")