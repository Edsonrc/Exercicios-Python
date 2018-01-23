'''
Construir um algoritmo que calcule a Área da Parede
e a quantidade de tinta a ser usada
Nome: Edson Ricardo Czarneski
Disciplina: Programação II - Python
Data: 13/01/2018

'''

l = float(input('Qual a largura da parede? '))
h = float(input('Qual a altura da parede? '))
a = l * h
t = a/2
print('Sua parede tem a dimensão de {:.2f} x {:.2f} m e uma área de {:.2f} m². '.format(l, h, a))
print('Para pintar esta parede, você precisará de {:.2f} litros de tinta.'.format(t))
