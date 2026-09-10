total_faturado = 0.0
quantidade_dias = 5
# range(1, 6) gera os dias 1, 2, 3, 4 e 5
for dia in range(1, quantidade_dias + 1):
    faturamento_dia = float(input(f"Digite o faturamento do dia {dia} (R$): "))
    total_faturado += faturamento_dia

media_diaria = total_faturado / quantidade_dias
print(f"\nTotal arrecadado no período: R$ {total_faturado:.2f}")
print(f"Média diária apurada: R$ {media_diaria:.2f}")

# PARTE 2: Inspeção de Caracteres em uma String (Token de Segurança)
print("\n" + "-" * 55)
print("MÓDULO DE SEGURANÇA: ANÁLISE DE CHAVE DE ACESSO")
print("-" * 55)

# A string representa a esteira de caracteres a ser percorrida
token_acesso = "SENAC-2026-POA"
total_hifens = 0
total_digitos = 0
total_letras = 0
print(f"Inspecionando os caracteres da chave:{token_acesso}\n")

# O laço for retira um caractere por vez da string
for caractere in token_acesso:
    if caractere == "-":
        total_hifens += 1
        print(f"Caractere '{caractere}' -> Separador de bloco detectado.")
    elif caractere >= "0" and caractere <= "9":
        total_digitos += 1
        print(f"Caractere '{caractere}' -> Dígito numérico registrado.")
    else:
        total_letras += 1
        print(f"Caractere '{caractere}' -> Letra identificada.")

# Relatório final após a conclusão do laço
print("\n" + "-" * 55)
print("RESUMO DA ESTRUTURA DA CHAVE:")
print(f"Letras encontradas: {total_letras}")
print(f"Dígitos numéricos: {total_digitos}")
print(f"Separadores (hifens): {total_hifens}")
print("-" * 55)