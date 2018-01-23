'''
Construir um algoritmo que faça a conversão de
Cº para Fº
Nome: Edson Ricardo Czarneski
Disciplina: Programação II - Python
Data: 13/01/2018

'''
celsius = float(input('Digite a sua temperatura: Cº'))
fare = ((9 * celsius) / 5) + 32
print('A temperatura {:.2f} Cº equivale a {:.2f} Fº.'.format(celsius, fare))
