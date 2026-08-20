# exercício 3: **Conversão de Temperatura**
# Peça ao usuário para inserir uma temperatura em Celsius e converta para Fahrenheit.

temp = int(input("Digite a temperatura em Celsius (ºC): "))

print("\n")

print(f"A temperatura em Celsius: {temp} ºC")

print(f"A temperatura em Fahrenheit: {32+(temp * 9)/5} ºF")