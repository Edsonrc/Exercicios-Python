'''
Criar uma lista com os nomes dos alunos para uma
apresentação de trabalhos
Nome: Edson Ricardo Czarneski
Disciplina: Programação II - Python
Data: 23/01/2018

'''
from random import shuffle
n1 = input('Digite o nome do Primeiro Aluno: ')
n2 = input('Digite o nome do Segundo Aluno: ')
n3 = input('Digite o nome do Terceiro Aluno: ')
n4 = input('Digite o nome do Quarto Aluno: ')

lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)

