'''
Construir um algoritmo que calcule o valor do novo salário
com reajuste
Nome: Edson Ricardo Czarneski
Disciplina: Programação II - Python
Data: 13/01/2018

'''

salario = float(input('Digite o valor do funcionário: R$'))
porc = int(input('Digite o valor de reajuste em %: '))
novo = (salario * porc/100) + salario
print('O novo salário, com reajuste de {} % será de R$ {:.2f}'.format(porc, novo))
