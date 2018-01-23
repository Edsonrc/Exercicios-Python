'''
Apresentando na tela o valor inteiro de um número
real
Nome: Edson Ricardo Czarneski
Disciplina: Programação II - Python
Data: 19/01/2018

'''

from math import trunc

num = float(input('Digite um valor: '))
trun = trunc(num)
print('O valor digitado é de {} e o sua porção inteira é de {}'.format(num, trun))
