'''Exercício 5: Validador de Senha com Limite de Tentativas (Contador com Parada
Antecipada)
● Objetivo: Controlar tentativas com contador e condição combinada (while tentativas <
limite and ...).
● Enunciado: Defina uma senha padrão no código (ex: "dev123"). O usuário tem no
máximo 3 tentativas para acertar a senha. A cada tentativa incorreta, informe quantas
tentativas ainda restam e incremente o contador. Se o usuário acertar, interrompa com a
mensagem "Acesso concedido". Se esgotar as 3 tentativas, exiba "Acesso bloqueado"'''

# Configurações iniciais
senha_padrao = 'dev123'
tentativas = 0
limite = 3

# Loop que roda enquanto o usuário tiver tentativas restantes
while tentativas < limite:
    senha = input('Digite a senha: ')
    tentativas += 1  # Incrementa a tentativa atual

    if senha == senha_padrao:
        print('Acesso concedido')
        break  # Interrompe o loop imediatamente se acertar
    else:
        restantes = limite - tentativas
        if restantes > 0:
            print(f'Senha incorreta! Você ainda tem {restantes} tentativa(s) restante(s).')
        else:
            print('Acesso bloqueado')
print('FIM')