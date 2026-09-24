cod='dev123'
contador=1
while contador <=3:
    senha=input('Digite a senha: ')
    if senha == cod:
        print('Acesso Concedido')
        break
    print(f'Senha INVÁLIDA! tentativa ({contador}/3)')
    contador+=1
print(f'Valor do contador depois do while --> {contador}')
if contador==4:
    print('Acesso Bloqueado!')
print('FIM')