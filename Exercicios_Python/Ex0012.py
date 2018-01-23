'''
Construir um algoritmo que calcule desconto
Nome: Edson Ricardo Czarneski
Disciplina: Programação II - Python
Data: 13/01/2018

'''
preco = float(input('Qual o valor do produto? R$'))
desc = preco - (preco * 5/100)
print('O produto que custava {:.2f}, na promoção com 5% de desconto, passa a valer {:.2f}'.format(preco, desc))
