'''
Calcular o valor da hipotenusa após apresentar os valores
dos catetos oposto e adjacente
Nome: Edson Ricardo Czarneski
Disciplina: Programação II - Python
Data: 19/01/2018

'''
from math import hypot

co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o Valor do Cateto Adjacente:'))
hip = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hip))

'''
Usando fórmula matemática
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o Valor do Cateto Adjacente:'))
hip = (co ** 2 + ca ** 2) ** (1/2) 
print('A hipotenusa vai medir {:.2f}'.format(hip))

'''

