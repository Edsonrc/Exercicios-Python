'''
Fazer o Dobro, a Raiz Quadrada e o Triplo
Nome: Edson Ricardo Czarneski
Disciplina: Programação II - Python
Data: 12/01/2018

'''
numero = int(input('Digite um número: '))
d = numero * 2
#r = numero ** (1/2)
r = pow(numero, (1/2))
t = numero * 3

print('Analisando o numero {}, temos: \n O dobro vale {} \n O triplo vale {} \n A Raiz Quadrada vale {:.2f}'.format(numero, d, t, r))
