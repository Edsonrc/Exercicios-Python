'''
Calcular o valor do seno, cosseno e tangente
de um ângulo
Nome: Edson Ricardo Czarneski
Disciplina: Programação II - Python
Data: 19/01/2018

'''
from math import sin, cos, tan, radians

ang = float(input('Digite o valor de um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O valor do seno é {:.2f}\nO valor do cosseno é {:.2f} \nO valor da tangente é {:.2f}.'.format(sen, cos, tan))

