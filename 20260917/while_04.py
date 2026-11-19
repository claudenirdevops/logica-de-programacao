'''Exercício 4: Média da Turma (Contador + Acumulador)
● Objetivo: Utilizar simultaneamente um contador de iterações e um acumulador de valores.
● Enunciado: Um professor quer calcular a média de uma turma. O programa deve pedir
notas (float) aos alunos continuamente até que seja digitada a nota -1 (condição de
parada). Durante a repetição, mantenha:
○ Uma variável acumuladora para somar as notas digitadas;
○ Uma variável contadora para registrar quantos alunos tiveram suas notas inseridas.
Ao encerrar o laço, calcule e exiba a média
aritmética simples (Soma / Quantidade).
Trate o caso em que nenhum aluno for inserido
antes do -1.'''

nota=float(input('Digite Primeira NOTA:'))
soma=0
contador=0
while nota != -1:
    soma+=nota
    contador+=1
    nota = float(input('Digite Próxima NOTA:'))
if contador==0:
    print ('Não houve digitação de Notas')
else:
    print(f'Média da Turma = {(soma / contador):.2f}')
print ("FIM")