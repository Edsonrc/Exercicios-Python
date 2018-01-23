'''
Digitando um número na tela, mostre o seu sucessor e
o seu antecessor
Nome: Edson Ricardo Czarneski
Disciplina: Programação II - Python
Data: 12/01/2018

'''

numero = int(input('Digite um número :'))
ant = numero - 1
suc = numero + 1
print('Você digitou o número {}. Seu antecessor é {} e seu sucessor é {}'.format(numero, ant, suc))
